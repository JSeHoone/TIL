package com.example.keep_alive;

import static org.assertj.core.api.Assertions.assertThat;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.boot.test.web.server.LocalServerPort;

@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class ConnectionCloseTests {

	private static final int REQUEST_COUNT = 1000;

	@LocalServerPort
	private int port;

	@Test
	@DisplayName("Connection: close로 요청하면 응답 코드가 200이다")
	void pingWithConnectionClose() throws IOException {
		long startTime = System.nanoTime();

		for (int i = 0; i < REQUEST_COUNT; i++) {
			HttpURLConnection con =
					(HttpURLConnection)
							new URL(
									"http://localhost:" + port + "/ping"
							).openConnection();

			con.setRequestProperty(
					"Connection",
					"close"
			);

			int responseCode = con.getResponseCode();

			System.out.println(
					responseCode
			);

			try (var inputStream = con.getInputStream()) {
				System.out.println(
						new String(inputStream.readAllBytes(), StandardCharsets.UTF_8)
				);
			}

			assertThat(responseCode).isEqualTo(200);
			con.disconnect();
		}

		printElapsedTime("Connection: close", startTime);
	}

	@Test
	@DisplayName("Connection: keep-alive로 요청하면 응답 코드가 200이다")
	void pingWithConnectionKeepAlive() throws IOException {
		long startTime = System.nanoTime();

		for (int i = 0; i < REQUEST_COUNT; i++) {
			HttpURLConnection con =
					(HttpURLConnection)
							new URL(
									"http://localhost:" + port + "/ping"
							).openConnection();

			con.setRequestProperty(
					"Connection",
					"keep-alive"
			);

			int responseCode = con.getResponseCode();

			System.out.println(
					responseCode
			);

			assertThat(responseCode).isEqualTo(200);

			try (var inputStream = con.getInputStream()) {
				System.out.println(
						new String(inputStream.readAllBytes(), StandardCharsets.UTF_8)
				);
			}
		}

		printElapsedTime("Connection: keep-alive", startTime);
	}

	private void printElapsedTime(String connectionType, long startTime) {
		long elapsedTime = System.nanoTime() - startTime;
		double elapsedMillis = elapsedTime / 1_000_000.0;

		System.out.printf(
				"%s 요청 %d회 처리 시간: %.3f ms%n",
				connectionType,
				REQUEST_COUNT,
				elapsedMillis
		);
	}

}
