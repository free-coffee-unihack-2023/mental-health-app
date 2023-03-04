import 'dart:io';
import 'package:http/http.dart' as http;
import 'dart:convert';

class WebServiceHelper {
  final _url;

  WebServiceHelper(this._url);

  Future getData() async {
    http.Response response = await http.get(this._url);
    return _responseHandler(response);
  }

  Future postData(Map requestBody) async {
    http.Response response = await http.post(
      this._url,
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: jsonEncode(requestBody),
    );
    return _responseHandler(response);
  }

  Future putData(Map requestBody) async {
    http.Response response = await http.put(
      this._url,
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: jsonEncode(requestBody),
    );
    return _responseHandler(response);
  }

  Future patchData(Map requestBody) async {
    http.Response response = await http.patch(
      this._url,
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: jsonEncode(requestBody),
    );
    return _responseHandler(response);
  }

  Future deleteData() async {
    http.Response response = await http.delete(
      this._url,
    );
    return _responseHandler(response);
  }

  dynamic _responseHandler(http.Response response) {
    if (response.statusCode == 200) {
      if (response.body != "") {
        String data = response.body;
        return jsonDecode(data);
      } else {
        return response.statusCode;
      }
    } else {
      print(response.body);
      return response.statusCode;
    }
  }
}