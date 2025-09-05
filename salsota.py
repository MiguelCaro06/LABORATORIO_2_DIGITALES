# -*- coding: utf-8 -*-
from naoqi import ALProxy
import time, math

IP = "192.168.0.106"
PORT = 9559

motion   = ALProxy("ALMotion", IP, PORT)
posture  = ALProxy("ALRobotPosture", IP, PORT)

if not motion.robotIsWakeUp():
    motion.wakeUp()
posture.goToPosture("StandInit", 0.6)

try:
    motion.setBreathEnabled("Body", False)
except:
    pass

motion.setStiffnesses("Body", 1.0)

# -------- Baile inicial (20s) --------
duration = 20.0
t0 = time.time()
dt = 0.05
f_base   = 0.35
f_hips   = 0.6
f_head   = 0.5
f_arms   = 0.45

vy_amp   = 0.20
w_amp    = 0.12
hip_amp  = 0.10
head_yaw_amp   = 0.25
head_pitch_amp = 0.08
lsp_base = 1.0
rsp_base = 1.0
sr_amp   = 0.18
el_amp   = 0.20

speed = 0.25

def safe_set(j, a):
    try:
        motion.setAngles(j, a, speed)
    except:
        pass

while (time.time() - t0) < duration:
    t = time.time() - t0
    ph_base = 2*math.pi*f_base*t
    ph_hip  = 2*math.pi*f_hips*t
    ph_head = 2*math.pi*f_head*t
    ph_arm  = 2*math.pi*f_arms*t

    vy      = vy_amp * math.sin(ph_base)
    vtheta  = w_amp  * math.sin(ph_base + math.pi/2.0)
    motion.moveToward(0.0, vy, vtheta)

    safe_set("HipRoll",  hip_amp * math.sin(ph_hip))
    safe_set("HipPitch", 0.05 + 0.03 * math.sin(ph_hip))

    safe_set("HeadYaw",   head_yaw_amp   * math.sin(ph_head))
    safe_set("HeadPitch", -0.03 + head_pitch_amp * math.sin(ph_head + math.pi/2.0))

    lsp = lsp_base + 0.4 * math.sin(ph_arm + math.pi/2.0)
    rsp = rsp_base + 0.4 * math.sin(ph_arm - math.pi/2.0)
    safe_set("LShoulderPitch", lsp)
    safe_set("RShoulderPitch", rsp)

    safe_set("LShoulderRoll",  sr_amp * math.sin(ph_arm))
    safe_set("RShoulderRoll", -sr_amp * math.sin(ph_arm))

    safe_set("LElbowRoll", -0.4 + (-el_amp) * math.sin(ph_arm + math.pi/3.0))
    safe_set("RElbowRoll",  0.4 + ( el_amp) * math.sin(ph_arm + math.pi/3.0))

    time.sleep(dt)

motion.moveToward(0.0, 0.0, 0.0)
motion.stopMove()

# -------- Giro 360° en 4 pasos de 90° --------
for i in range(4):
    motion.moveTo(0.0, 0.0, math.pi/2, [["MaxVelTheta", 0.4]])
    time.sleep(0.5)

# -------- Movimiento lateral de derecha a izquierda --------
duration = 15.0
t0 = time.time()
vy_amp   = 0.25
w_amp    = 0.10

while (time.time() - t0) < duration:
    t = time.time() - t0
    ph = 2*math.pi*0.3*t
    vy = vy_amp * math.sin(ph)
    vtheta = w_amp * math.sin(ph + math.pi/2.0)
    motion.moveToward(0.0, vy, vtheta)
    time.sleep(0.05)

motion.moveToward(0.0, 0.0, 0.0)
motion.stopMove()
posture.goToPosture("StandInit", 0.6)

