resource "helm_release" "yantram-apache" {
  name = "yantram-apache"
//  repository = "https://github.com/mozilla/DeepSpeech-examples/tree/r0.8/python_websocket_server/helm"
  repository = "https://github.com/mozilla/DeepSpeech-examples/python_websocket_server/helm/deepspeech-server"
  chart = "deepspeech-server"
}

//DeepSpeech-examples/python_websocket_server/helm/deepspeech-server/