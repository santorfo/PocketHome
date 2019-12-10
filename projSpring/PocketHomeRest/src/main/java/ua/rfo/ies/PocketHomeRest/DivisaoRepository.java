package ua.rfo.ies.PocketHomeRest;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DivisaoRepository extends JpaRepository<Divisao, Long>{
	List<Divisao> findByhouseId(long houseId);
	
	Divisao findById(long id);

}
