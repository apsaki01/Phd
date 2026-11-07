# Rehearsal feedback — iteration 222 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[target,door] lock -> [when teammate_inside] grab ramp to away_from_opponent[yaw0,door] lock release | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.628
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.23, "door_blocking": 0.75, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 41.4
- doors sealed+locked at prep end: 0.81, ramp inside quadrant at prep end: 0.07
- seekers entered quadrant: 0.28, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.64, 0.74] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@73; prep1/0:done@13; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.88, 1.6] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:no_object@32; play0/1:timeout@71; prep1/0:dropped@13; prep1/0:done@22; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.32, 1.59] | seeker 3 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@14; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; prep1/0:done@19; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@74
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.1, 0.07] | seeker 2 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@28; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:no_target@29; prep1/1:dropped@30; play1/0:no_object@32; play1/1:no_target@33
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.81, 1.39] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; prep1/0:done@14; prep1/1:no_target@15; play1/0:dropped@32; play1/0:no_object@32; play1/1:done@34
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.0, 1.12] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@35; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@72
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.7, 0.58] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@12; prep0/0:done@29; play0/0:dropped@32; play0/0:no_object@32; play0/1:timeout@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@75
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.41, 1.03] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; play0/0:dropped@32; play0/0:no_object@32; play0/1:timeout@71; play1/0:timeout@70; play1/1:no_target@71