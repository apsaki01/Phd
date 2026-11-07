# Rehearsal feedback — iteration 8 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.0, 'damp': 0.5, 'tol': 0.4, 'offset': 0.25, 'seg_timeout': 30.0}
  role0 prep: [when doors_sealed] grab box to wander[align,door] release | play: stay then [when ramp_inside] grab ramp to stay[yaw1,door] lock
  role1 prep: [when doors_sealed] grab ramp to wander[align,door] release | play: stay then [when ramp_inside] grab box to stay[yaw2,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.574
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.0, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 33.8
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.65, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 37 (hider outside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | hiders never seen | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30