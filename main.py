import bbcon, arbitrator, Sensob, motob
from Behaviors import check_wall, follow_line, Front_collision, Side_collision
from basic_robot import camera, irproximity_sensor, reflectance_sensors, ultrasonic, zumo_button

# Initialize all objects
bb = bbcon.Bbcon()
cw = check_wall.CheckWall(bb, 1)
fc = Front_collision.FrontCollision(bb, 2)
sc = Side_collision.SideCollision(bb, 3)
fl = follow_line.FollowLine(bb, 4)
a = arbitrator.Arbitrator(bb)
cam = Sensob.Sensob()
ir = Sensob.Sensob()
ultrasound = Sensob.Sensob()
rs = Sensob.Sensob()
motor = motob.Motob()

# Add sensors to sensob
cam.add_sensor(camera.Camera())
ir.add_sensor(irproximity_sensor.IRProximitySensor())
ultrasound.add_sensor(ultrasonic.Ultrasonic())
rs.add_sensor(reflectance_sensors.ReflectanceSensors())

# Add sensobs to behaviors
cw.set_sensob(cam)
fc.set_sensob(ultrasound)
sc.set_sensob(ir)
fl.set_sensob(rs)

# Add stuff to bbcon object
bb.add_sensob([cam, ir, ultrasonic, rs])
bb.add_behavior([cw, fc, sc, fl])
bb.arbitrator = a
bb.motob = motor

zumo_button.ZumoButton().wait_for_press()
while bb.run_one_timestep():
    continue
