(define (problem LegoProblem2d) (:domain LegoWorld2d)            

                (:objects 
                    r0 r1 r2 r3 r4 c0 c1 c2 c3 c4
                )

                
                (:init

     (on_ground r0 c0)
     (occupied r0 c0)
      (on_ground r0 c1)
     (moveable r0 c1)
     (clear r0 c2)
     (clear r0 c3)
     (clear r0 c4)
     (occupied r1 c0)
      (clear r1 c1)
     (clear r1 c2)
     (clear r1 c3)
     (clear r1 c4)
     (occupied r2 c0)
      (clear r2 c1)
     (clear r2 c2)
     (clear r2 c3)
     (clear r2 c4)
     (moveable r3 c0)
     (clear r3 c1)
     (clear r3 c2)
     (clear r3 c3)
     (clear r3 c4)
     (clear r4 c0)
     (clear r4 c1)
     (clear r4 c2)
     (clear r4 c3)
     (clear r4 c4)

    
                )

                (:goal (and

     (clear r0 c0)
     (on_ground r0 c1)
     (occupied r0 c1)
      (on_ground r0 c2)
     (moveable r0 c2)
     (clear r0 c3)
     (clear r0 c4)
     (clear r1 c0)
     (occupied r1 c1)
      (clear r1 c2)
     (clear r1 c3)
     (clear r1 c4)
     (clear r2 c0)
     (occupied r2 c1)
      (clear r2 c2)
     (clear r2 c3)
     (clear r2 c4)
     (clear r3 c0)
     (moveable r3 c1)
     (clear r3 c2)
     (clear r3 c3)
     (clear r3 c4)
     (clear r4 c0)
     (clear r4 c1)
     (clear r4 c2)
     (clear r4 c3)
     (clear r4 c4)


                ))
                )