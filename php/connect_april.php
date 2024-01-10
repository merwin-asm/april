<?php

class ConnectApril {
    public static function recv_request() {
        $n = $argv[1];
        $filePath = "./{$n}.input";

        try {
            $data = file_get_contents($filePath);
            return json_decode($data, true);
        } catch (Exception $e) {
            echo "Error reading file: {$filePath}\n";
            return null;
        }
    }

    public static function send_response($response) {
        $n = $argv[1];
        $filePath = "./{$n}.output";

        try {
            file_put_contents($filePath, json_encode($response));
        } catch (Exception $e) {
            echo "Error writing file: {$filePath}\n";
        }
    }
}
?>

