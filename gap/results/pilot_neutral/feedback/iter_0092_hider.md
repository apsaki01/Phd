# Rehearsal feedback — iteration 92 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.47, 'tol': 0.32, 'offset': 0.16, 'seg_timeout': 36.54}
  role0 prep: (none) | play: segments then to door_block[yaw0,door] release -> grab box to stay[yaw3,door] lock -> [when opponent_visible] to door_inside[yaw2,door]
  role1 prep: (none) | play: segments then to door_block[yaw0,door] release -> grab box to stay[yaw3,door] lock -> [when opponent_visible] to door_inside[yaw2,door]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.284
- hider win-rate: 0.25
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.2
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.90, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@41; play0/1:timeout@78; play0/2:dropped@79; play1/0:done@38; play1/1:timeout@75; play1/2:dropped@76
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 54 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@39; play0/1:timeout@76; play1/0:done@41; play1/1:timeout@78
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@37; play0/1:timeout@74; play0/2:dropped@75; play1/0:done@45
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@38; play0/1:timeout@75; play0/2:dropped@77; play1/0:done@42; play1/1:dropped@69; play1/1:dropped@74; play1/1:timeout@79
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@40; play0/1:timeout@77; play0/2:dropped@78; play1/0:done@35; play1/1:dropped@43; play1/1:timeout@72; play1/2:dropped@74
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@36; play0/1:timeout@73; play0/2:dropped@77; play1/0:no_target@32; play1/1:timeout@69; play1/2:dropped@71; play1/2:no_target@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@38; play0/1:timeout@75; play1/0:no_target@32; play1/1:timeout@69; play1/2:no_target@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@42; play0/1:dropped@47; play0/1:dropped@53; play0/1:dropped@56; play0/1:timeout@79; play1/0:no_target@32; play1/1:timeout@69; play1/2:dropped@74; play1/2:no_target@74