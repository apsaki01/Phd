# Rehearsal feedback — iteration 138 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.52, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 38.83}
  role0 prep: grab box to climb[yaw3,door] release -> [when ramp_inside] grab ramp to climb[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[yaw3,door] release -> [when ramp_inside] grab ramp to climb[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.286
- hider win-rate: 0.23
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 35.8
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.85, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.96, 1.05] | hiders never seen | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play0/2:dropped@77; prep1/0:done@11; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.84, 0.63] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@15; play1/0:dropped@32; play1/0:dropped@37; play1/0:done@53
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.43, 1.29] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@9; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@5; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.08, 1.8] | seeker 2 saw hider 0 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; play0/0:dropped@32; play0/0:dropped@44; play0/0:dropped@52; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@21; play1/0:dropped@32; play1/0:dropped@41; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.4, 0.45] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:no_object@14; play0/0:done@45; prep1/0:done@14; prep1/1:dropped@15; prep1/1:done@16; play1/0:dropped@32; play1/0:dropped@58; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.77, 0.3] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:dropped@2; prep1/0:done@8; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.88, 0.64] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@18; play1/0:dropped@32; play1/0:dropped@40; play1/0:dropped@49; play1/0:dropped@53; play1/0:dropped@61; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.26, 0.39] | seeker 2 saw hider 0 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play0/2:dropped@75; prep1/0:done@4; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71