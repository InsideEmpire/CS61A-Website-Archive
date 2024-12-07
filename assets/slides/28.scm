; Let example

(define (star n m) 
  (let ((a (/ (* 360 m) n)))
    (define (side k) 
      (if (< k n) (begin (fd 100) (rt a) (side (+ k 1))))) 
    (side 0)))

; List demos

(define s (cons 1 (cons 2 nil)))
(cons 3 s)
(cons 4 (cons 3 s))
(cons (cons 4 (cons 3 nil)) s)
(car (car (cons (cons 4 (cons 3 nil)) s)))
(cons s (cons s nil))

(list? s)
(list? nil)
(list? 4)
(null? nil)
(null? s)

(list 1 2)
(list 1 2 3 4)
(cdr (list 1 2 3 4))
(cons 0 (cdr (list 1 2 3 4)))

(list s)
(list 3 s)
(cons 3 s)
(list s s)
(cons s s)

;;; Return a list of two lists; the first n elements of s and the rest
;;; scm> (split (list 3 4 5 6 7 8) 3)
;;; ((3 4 5) (6 7 8))
(define (split s n)
  ; The first n elements of s
  (define (prefix s n)
    (if (zero? n) nil (cons (car s) (prefix (cdr s) (- n 1)))))
  ; The elements after the first n
  (define (suffix s n)
    (if (zero? n) s (suffix (cdr s) (- n 1))))
  (list (prefix s n) (suffix s n)))


(define (split s n)
  (if (= n 0) 
      (list nil s) 
      (let ((split-rest (split (cdr s) (- n 1)))) 
	(cons (cons (car s) (car split-rest)) 
	      (cdr split-rest)))))

; Quotation demos

'(1 2 3)
(quote (1 2 3))
'(1 (2 3) 4)
(car (cdr (car (cdr '(1 (2 3) 4)))))
(car (cdr (car (cdr '(a (b c) d)))))
'(+ 1 2)
(car (quote (+ 1 2)))
(car '(+ 1 2))
(cons '+ (list 1 2))

