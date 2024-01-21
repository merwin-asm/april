;;; ConnectApril.lisp

(defun recv-request ()
  (let ((n (parse-integer (car (last *command-line-argument-list*)))))
    (with-open-file (file (format nil "~a.input" n) :direction :input)
      (let ((data (read file)))
        (if (consp data)
            data
            nil)))))

(defun send-response (response)
  (let ((n (parse-integer (car (last *command-line-argument-list*)))))
    (with-open-file (file (format nil "~a.output" n) :direction :output)
      (prin1 response file))))