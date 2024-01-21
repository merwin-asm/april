classdef ConnectApril
    methods(Static)
        function requestData = recv_request()
            n = str2double(varargin{end});
            filePath = sprintf('.%d.input', n);

            try
                data = fileread(filePath);
                requestData = jsondecode(data);
            catch
                fprintf('Error reading input file\n');
                requestData = [];
            end
        end

        function send_response(response)
            n = str2double(varargin{end});
            filePath = sprintf('.%d.output', n);

            try
                jsonStr = jsonencode(response);
                fid = fopen(filePath, 'w');
                fwrite(fid, jsonStr);
                fclose(fid);
            catch
                fprintf('Error writing output file\n');
            end
        end
    end
end