**FREE

dcl-ds RequestData qualified;
  message varchar(100);
end-ds;

dcl-ds ResponseData qualified;
  message varchar(100);
end-ds;

begsr Main;

  RequestData = recvRequest();
  ResponseData.message = 'Hello, RPG!';
  sendResponse(ResponseData);

endsr;

dcl-proc recvRequest;
  dcl-s n packed(5);
  n = %int(%char(%parms));

  dcl-s filePath varchar(20);
  filePath = '.' + %trim(%editc(n:'X')) + '.input';

  exec sql SET OPTION COMMIT = *NONE;
  exec sql INCLUDE 'QRPGLESRC/QUICKIO';
  exec sql DECLARE C1 CURSOR FOR
    SELECT * FROM :filePath FOR READ ONLY;
  exec sql OPEN C1;
  exec sql FETCH C1 INTO :RequestData;
  exec sql CLOSE C1;

end-proc;

dcl-proc sendResponse;
  dcl-s filePath varchar(20);
  filePath = '.' + %trim(%editc(n:'X')) + '.output';

  exec sql SET OPTION COMMIT = *NONE;
  exec sql INCLUDE 'QRPGLESRC/QUICKIO';
  exec sql DECLARE C2 CURSOR FOR
    SELECT * FROM :filePath FOR WRITE ONLY;
  exec sql OPEN C2;
  exec sql FETCH C2 INTO :ResponseData;
  exec sql CLOSE C2;

end-proc;
