(define (problem LegoWorld2dProblem) (:domain LegoWorld2d)

(:objects
    r0 r1 r2 r3 r4 c0 c1 c2 c3 c4
)
(:init

 (clear r0 c0)
 (not (occupied r0 c0))
 (clear r0 c1)
 (not (occupied r0 c1))
 (clear r0 c2)
 (not (occupied r0 c2))
 (clear r0 c3)
 (not (occupied r0 c3))
 (occupied r0 c4)
 (not (clear r0 c4))
 (trapped r0 c4)
 (clear r1 c0)
 (not (occupied r1 c0))
 (clear r1 c1)
 (not (occupied r1 c1))
 (clear r1 c2)
 (not (occupied r1 c2))
 (clear r1 c3)
 (not (occupied r1 c3))
 (occupied r1 c4)
 (not (clear r1 c4))
 (trapped r1 c4)
 (clear r2 c0)
 (not (occupied r2 c0))
 (clear r2 c1)
 (not (occupied r2 c1))
 (clear r2 c2)
 (not (occupied r2 c2))
 (clear r2 c3)
 (not (occupied r2 c3))
 (occupied r2 c4)
 (not (clear r2 c4))
 (trapped r2 c4)
 (clear r3 c0)
 (not (occupied r3 c0))
 (clear r3 c1)
 (not (occupied r3 c1))
 (clear r3 c2)
 (not (occupied r3 c2))
 (clear r3 c3)
 (not (occupied r3 c3))
 (occupied r3 c4)
 (not (clear r3 c4))
 (trapped r3 c4)
 (clear r4 c0)
 (not (occupied r4 c0))
 (clear r4 c1)
 (not (occupied r4 c1))
 (clear r4 c2)
 (not (occupied r4 c2))
 (clear r4 c3)
 (not (occupied r4 c3))
 (occupied r4 c4)
 (not (clear r4 c4))



)

(:goal (and

 (clear r0 c0)
 (not (occupied r0 c0))
 (clear r0 c1)
 (not (occupied r0 c1))
 (clear r0 c2)
 (not (occupied r0 c2))
 (occupied r0 c3)
 (not (clear r0 c3))
 (occupied r0 c4)
 (not (clear r0 c4))
 (trapped r0 c4)
 (clear r1 c0)
 (not (occupied r1 c0))
 (clear r1 c1)
 (not (occupied r1 c1))
 (clear r1 c2)
 (not (occupied r1 c2))
 (clear r1 c3)
 (not (occupied r1 c3))
 (occupied r1 c4)
 (not (clear r1 c4))
 (trapped r1 c4)
 (clear r2 c0)
 (not (occupied r2 c0))
 (clear r2 c1)
 (not (occupied r2 c1))
 (clear r2 c2)
 (not (occupied r2 c2))
 (clear r2 c3)
 (not (occupied r2 c3))
 (occupied r2 c4)
 (not (clear r2 c4))
 (trapped r2 c4)
 (clear r3 c0)
 (not (occupied r3 c0))
 (clear r3 c1)
 (not (occupied r3 c1))
 (clear r3 c2)
 (not (occupied r3 c2))
 (clear r3 c3)
 (not (occupied r3 c3))
 (occupied r3 c4)
 (not (clear r3 c4))
 (clear r4 c0)
 (not (occupied r4 c0))
 (clear r4 c1)
 (not (occupied r4 c1))
 (clear r4 c2)
 (not (occupied r4 c2))
 (clear r4 c3)
 (not (occupied r4 c3))
 (clear r4 c4)
 (not (occupied r4 c4))



))

)
