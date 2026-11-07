# Rehearsal feedback — iteration 102 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.52, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 36.54}
  role0 prep: [when teammate_inside] grab ramp to climb[align,door] release | play: segments then to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock -> [when opponent_visible] to door_inside[yaw2,door]
  role1 prep: [when teammate_inside] grab ramp to climb[align,door] release | play: segments then to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock -> [when opponent_visible] to door_inside[yaw2,door]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.319
- hider win-rate: 0.25
- behaviour detection rates: {"chasing": 0.3, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.4}
- mean first-seen play step: 34.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.47
- seekers entered quadrant: 0.88, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@69; play0/2:dropped@70; play0/2:done@74; play1/0:done@32; play1/1:timeout@69; play1/2:dropped@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:dropped@46; play0/1:dropped@49; play0/1:timeout@69; play0/2:dropped@72; play1/0:done@32; play1/1:timeout@69; play1/2:dropped@72; play1/2:no_target@72
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@69; play0/2:dropped@73; play1/0:done@32; play1/1:timeout@69; play1/2:dropped@73
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.92, 0.0] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; play0/0:dropped@32; play0/0:done@32; play0/1:timeout@69; play0/2:dropped@70; play0/2:done@71; prep1/0:no_object@0; play1/0:done@32; play1/1:timeout@69; play1/2:dropped@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:dropped@43; play0/1:timeout@69; play1/0:done@32; play1/1:timeout@69
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@69; play1/0:done@32; play1/1:dropped@44; play1/1:timeout@69
- p_door=0.25 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@69; play1/0:timeout@68; play1/1:dropped@69
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.87] | seeker 2 saw hider 0 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@28; play0/0:dropped@32; play0/0:done@32; play0/1:timeout@69; prep1/0:no_object@26; play1/0:done@32; play1/1:timeout@69