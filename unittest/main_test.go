package main

import (
    "net/http"
    "net/http/httptest"
    "testing"
    "strings"

    "github.com/stretchr/testify/assert"
)

// go get github.com/stretchr/testify/assert が必要

func TestHandler(t *testing.T) {
    req := httptest.NewRequest("GET", "/", nil)
    rr := httptest.NewRecorder()
    handler(rr, req)

    assert.Equal(t, http.StatusOK, rr.Code)

    responseBody := strings.TrimSpace(rr.Body.String())
    expected := `{"message":"Hello, World!"}`
    assert.Equal(t, expected, responseBody)
}