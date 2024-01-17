# connect_april.rb

require 'json'

module ConnectApril
  def self.recv_request
    n = ARGV[-1]
    file_path = ".#{n}.input"

    begin
      data = File.read(file_path)
      JSON.parse(data)
    rescue StandardError => e
      puts "Error reading file: #{file_path}"
      nil
    end
  end

  def self.send_response(response)
    n = ARGV[-1]
    file_path = ".#{n}.output"

    begin
      File.write(file_path, JSON.generate(response))
    rescue StandardError => e
      puts "Error writing file: #{file_path}"
    end
  end
end

