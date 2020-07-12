package streami.co.adminserver;

import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    private static final String template = "User: %s";
    private final AtomicLong loginCounter = new AtomicLong();

    @GetMapping("/login")
    public User loginAction(
             @RequestParam(value = "name", defaultValue = "World") String name) {
        return new User(loginCounter.incrementAndGet(), String.format(template, name));
    }
}
