package main

import (
    "net/http"
    "encoding/json"

)

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
    // Write your prompt here.
}
