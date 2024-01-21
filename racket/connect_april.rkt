#lang racket

(define (recv-request)
  (let ((n (vector-ref (current-command-line-arguments) (sub1 (vector-length (current-command-line-arguments)))))
        (file-path (format "~a.input" n)))
    (with-handlers ([exn:fail:filesystem? (lambda (exn) #f)])
      (call-with-input-file file-path
        (lambda (input)
          (let ((data (read-json input)))
            data))))))

(define (send-response response)
  (let* ((n (vector-ref (current-command-line-arguments) (sub1 (vector-length (current-command-line-arguments)))))
         (file-path (format "~a.output" n)))
    (with-handlers ([exn:fail:filesystem? (lambda (exn) (displayln (exn-message exn)))])
      (call-with-output-file file-path
        (lambda (output)
          (write-json response output))))))