import 'dart:io';
import 'package:http/http.dart' as http;
import 'dart:convert';

class WebServiceHelper {
  final _apiKey;
  final _url;

  WebServiceHelper(this._url, this._apiKey);

  Future getData(String acceptHeader) async {
    http.Response response = await http.get(
      this._url,
      headers: {
        HttpHeaders.acceptHeader: acceptHeader,
        HttpHeaders.authorizationHeader: this._apiKey,
      },
    );
    return _responseHandler(response);
  }

  Future postData(
      Map requestBody, String acceptHeader, String contentType) async {
    http.Response response = await http.post(
      this._url,
      headers: {
        HttpHeaders.acceptHeader: acceptHeader,
        HttpHeaders.authorizationHeader: this._apiKey,
        HttpHeaders.contentTypeHeader: contentType
      },
      body: jsonEncode(requestBody),
    );
    return _responseHandler(response);
  }

  Future putData(
      Map requestBody, String acceptHeader, String contentType) async {
    http.Response response = await http.put(
      this._url,
      headers: {
        HttpHeaders.acceptHeader: acceptHeader,
        HttpHeaders.authorizationHeader: this._apiKey,
        HttpHeaders.contentTypeHeader: contentType
      },
      body: jsonEncode(requestBody),
    );
    return _responseHandler(response);
  }

  Future patchData(
      Map requestBody, String acceptHeader, String contentType) async {
    http.Response response = await http.patch(
      this._url,
      headers: {
        HttpHeaders.acceptHeader: acceptHeader,
        HttpHeaders.authorizationHeader: this._apiKey,
        HttpHeaders.contentTypeHeader: contentType
      },
      body: jsonEncode(requestBody),
    );
    return _responseHandler(response);
  }

  Future deleteData(String acceptHeader) async {
    http.Response response = await http.delete(
      this._url,
      headers: {
        HttpHeaders.acceptHeader: acceptHeader,
        HttpHeaders.authorizationHeader: this._apiKey,
      },
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