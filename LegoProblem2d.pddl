(define (problem LegoProblem2d)
    (:domain plswork)
    (:objects
    r0 r1 r2 r3 r4 - row
    c0 c1 c2 c3 c4 - col
    )
    
    (:init
    (= (block_pos_row r0) 0)
    (= (block_pos_row r1) 1)
    (= (block_pos_row r2) 2)
    (= (block_pos_row r3) 3)
    (= (block_pos_row r4) 4)
    (= (block_pos_col c0) 0)
    (= (block_pos_col c1) 1)
    (= (block_pos_col c2) 2)
    (= (block_pos_col c3) 3)
    (= (block_pos_col c4) 4)
    (clear r0 c0)(on_ground r0 c0)(clear r0 c1)(on_ground r0 c1)(clear r0 c2)(on_ground r0 c2)(clear r0 c3)(on_ground r0 c3)(on_ground r0 c4)(not (moveable r0 c4))(clear r1 c0)(clear r1 c1)(clear r1 c2)(clear r1 c3)(not (moveable r1 c4))(clear r2 c0)(clear r2 c1)(clear r2 c2)(clear r2 c3)(not (moveable r2 c4))(clear r3 c0)(clear r3 c1)(clear r3 c2)(clear r3 c3)(not (moveable r3 c4))(clear r4 c0)(clear r4 c1)(clear r4 c2)(clear r4 c3)(moveable r4 c4)
    )
    (:goal
    (and
    (clear r0 c0)(on_ground r0 c0)(clear r0 c1)(on_ground r0 c1)(clear r0 c2)(on_ground r0 c2)(on_ground r0 c3)(moveable r0 c3)(on_ground r0 c4)(not (moveable r0 c4))(clear r1 c0)(clear r1 c1)(clear r1 c2)(clear r1 c3)(not (moveable r1 c4))(clear r2 c0)(clear r2 c1)(clear r2 c2)(clear r2 c3)(not (moveable r2 c4))(clear r3 c0)(clear r3 c1)(clear r3 c2)(clear r3 c3)(moveable r3 c4)(clear r4 c0)(clear r4 c1)(clear r4 c2)(clear r4 c3)(clear r4 c4)
    )
    )
    )
