package com.example.keep_alive;

import static org.assertj.core.api.Assertions.assertThat;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.boot.test.web.server.LocalServerPort;

@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class KeepAliveApplicationTests {

	private static final Pattern PORT_PATTERN = Pattern.compile("port=(\\d+)");

	@LocalServerPort
	private int port;

	@Test
	void contextLoads() {
	}

	@Test
	void pingKeepsAliveSameTcpConnection() throws IOException, InterruptedException {
		HttpClient client = HttpClient.newBuilder()
				.version(HttpClient.Version.HTTP_1_1)
				.build();

		HttpRequest request = HttpRequest.newBuilder()
				.uri(URI.create("http://localhost:" + port + "/ping"))
				.version(HttpClient.Version.HTTP_1_1)
				.GET()
				.build();

		HttpResponse<String> firstResponse = client.send(request, HttpResponse.BodyHandlers.ofString());
		HttpResponse<String> secondResponse = client.send(request, HttpResponse.BodyHandlers.ofString());

		assertThat(firstResponse.statusCode()).isEqualTo(200);
		assertThat(secondResponse.statusCode()).isEqualTo(200);
		assertThat(extractRemotePort(secondResponse.body())).isEqualTo(extractRemotePort(firstResponse.body()));
	}

	private int extractRemotePort(String body) {
		Matcher matcher = PORT_PATTERN.matcher(body);

		assertThat(matcher.find())
				.as("response body contains remote port: %s", body)
				.isTrue();

		return Integer.parseInt(matcher.group(1));
	}

}
