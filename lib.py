DECLARE 
	i_roll_no NUMBER;
	name_of_book VARCHAR2(25);
	no_of_days NUMBER;
	return_date DATE := TO_DATE(SYSDATE,'DD-MM-YYYY');
	temp NUMBER;
	doi DATE;
	fine NUMBER;
BEGIN
	i_roll_no := &i_roll_no;
	name_of_book := '&nameofbook';
	--dbms_output.put_line(return_date);
	SELECT to_date(borrower.dateofissue,'DD-MM-YYYY') INTO doi FROM borrower WHERE borrower.roll_no = i_roll_no AND borrower.name_of_book = name_of_book;
	no_of_days := return_date-doi;
	dbms_output.put_line(no_of_days);
	IF (no_of_days >15 AND no_of_days <=30) THEN
		fine := 5*no_of_days;
		
	ELSIF (no_of_days>30 ) THEN
		temp := no_of_days-30;
		fine := 150 + temp*50;
	END IF;
	dbms_output.put_line(fine);
	INSERT INTO fine VALUES(i_roll_no,return_date,fine);
	UPDATE borrower SET status = 'RETURNED' WHERE borrower.roll_no = i_roll_no;
	
	
END;