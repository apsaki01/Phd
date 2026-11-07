# Rehearsal feedback — iteration 122 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.52, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 38.83}
  role0 prep: [when teammate_inside] grab ramp to climb[align,door] release | play: segments then grab box to stay[yaw3,door] lock -> to stay[yaw0,door] release
  role1 prep: (none) | play: segments then grab box to stay[yaw3,door] lock -> to stay[yaw0,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.246
- hider win-rate: 0.12
- behaviour detection rates: {"chasing": 0.3, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.15}
- mean first-seen play step: 34.2
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.28
- seekers entered quadrant: 0.95, mean max seeker z: 0.23

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:dropped@59; play0/0:dropped@62; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:dropped@42; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@17; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71