import bbcon, arbitrator, sensob, motob
from Behaviors import check_wall, follow_line, front_collision, side_collision
from basic_robot import camera, irproximity_sensor, reflectance_sensors, ultrasonic, zumo_button

# Initialize all objects
bb = bbcon.Bbcon()
cw = check_wall.CheckWall(bb, 4)
fc = front_collision.FrontCollision(bb, 3)
sc = side_collision.SideCollision(bb, 2)
fl = follow_line.FollowLine(bb, 1)
a = arbitrator.Arbitrator(bb)
cam = sensob.Sensob()
ir = sensob.Sensob()
us = sensob.Sensob()
rs = sensob.Sensob()
motor = motob.Motob()

# Add sensors to sensob
cam.add_sensor(camera.Camera())
ir.add_sensor(irproximity_sensor.IRProximitySensor())
us.add_sensor(ultrasonic.Ultrasonic())
rs.add_sensor(reflectance_sensors.ReflectanceSensors())

# Add sensobs to behaviors
cw.set_sensob(cam)
# fc.set_sensob(us)
sc.set_sensob(ir)
fl.set_sensob(rs)

# Add stuff to bbcon object
bb.add_sensob([cam, ir, us, rs])
# bb.add_behavior([cw, fc, sc, fl])
bb.add_behavior([cw, sc, fl])
bb.arbitrator = a
bb.motob = motor

zumo_button.ZumoButton().wait_for_press()
while bb.run_one_timestep():
    continue
