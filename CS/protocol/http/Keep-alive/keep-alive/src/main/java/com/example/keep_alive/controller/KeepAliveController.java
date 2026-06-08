package com.example.keep_alive.controller;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class KeepAliveController {

    @GetMapping("/ping")
    public String ping(HttpServletRequest request) {

        System.out.println(
                Thread.currentThread().getName()
        );

        return """
                client=%s
                port=%d
                connection=%s
                """
                .formatted(
                        request.getRemoteAddr(),
                        request.getRemotePort(),
                        request.getHeader("Connection")
                );
    }
}
