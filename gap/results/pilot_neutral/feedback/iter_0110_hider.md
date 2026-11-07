# Rehearsal feedback — iteration 110 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.52, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 36.54}
  role0 prep: [when teammate_inside] grab ramp to climb[align,door] release | play: segments then grab box to stay[yaw3,door] lock -> to stay[yaw0,door] release -> [when opponent_visible] to door_inside[yaw2,door]
  role1 prep: [when teammate_inside] grab ramp to climb[align,door] release | play: segments then grab box to stay[yaw3,door] lock -> to stay[yaw0,door] release -> [when opponent_visible] to door_inside[yaw2,door]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.317
- hider win-rate: 0.25
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.3}
- mean first-seen play step: 36.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.42
- seekers entered quadrant: 0.93, mean max seeker z: 0.23

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; play0/0:dropped@32; play0/0:timeout@68; play0/1:dropped@69; play0/1:done@69; prep1/0:no_object@2; play1/0:timeout@68; play1/1:dropped@69; play1/1:done@69
- p_door=0.25 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.08] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_object@19; play0/0:timeout@68; play0/1:dropped@69; play0/1:done@69; prep1/0:done@22; play1/0:dropped@32; play1/0:timeout@68; play1/1:dropped@69; play1/1:done@69; play1/2:no_target@75
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; play0/1:dropped@69; play0/1:done@69; play0/2:done@78; play1/0:dropped@50; play1/0:timeout@68; play1/1:dropped@69; play1/1:done@69; play1/2:no_target@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.16) | segments: play0/0:timeout@68; play0/1:dropped@69; play0/1:done@69; play1/0:timeout@68; play1/1:dropped@69; play1/1:done@69; play1/2:no_target@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.72, 0.74] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; play0/0:dropped@32; play0/0:timeout@68; play0/1:dropped@69; play0/1:done@69; prep1/0:no_object@10; play1/0:timeout@68; play1/1:dropped@69; play1/1:done@69
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 51 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; play0/1:dropped@69; play0/1:done@69; play0/2:done@74; play1/0:timeout@68; play1/1:dropped@69; play1/1:done@69
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.48, 0.0] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; play0/0:dropped@32; play0/0:timeout@68; play0/1:dropped@69; play0/1:done@69; play0/2:done@77; prep1/0:no_object@21; play1/0:timeout@68; play1/1:dropped@69; play1/1:done@69; play1/2:no_target@70
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; play0/1:dropped@69; play0/1:done@69; play1/0:timeout@68; play1/1:dropped@69; play1/1:done@69