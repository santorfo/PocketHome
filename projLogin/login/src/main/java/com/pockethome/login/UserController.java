package com.pockethome.login;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
public class UserController {

    @Autowired
    private UserRepository userRepository;

    // Insert new user
    @PostMapping(value = "/users")
    public User newUser (@Valid @RequestBody User user){
        return userRepository.save(user);
    }

    // Get the user info
    @GetMapping(value = "/users/{id}")
    public User getUser (@PathVariable(value = "id") Long userId){
        return userRepository.findById(userId).get();
    }

    // Alter the user info
    @PutMapping(value = "/users/{id}")
    public User alterUser (@RequestBody User newusr, @PathVariable(value = "id") Long userId){
        User usr =  userRepository.findById(userId).get();
        usr.setFirstName(newusr.getFirstName());
        usr.setLastName(newusr.getLastName());
        usr.setEmail(newusr.getEmail());
        usr.setPassword(newusr.getPassword());
        return userRepository.save(usr);
    }
}