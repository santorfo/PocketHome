package ua.rfo.ies.PocketHomeRest;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CasaRepository extends JpaRepository<Casa, Long>{

}
