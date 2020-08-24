# Python_Basics
Simple programs for that allow for quick prototyping and reference

Example of what you would put in the ardunio code to print a .csv file. 
    Serial.print(",");
    Serial.print(timestep,DEC);
    Serial.print(",");
    Serial.print(EncoderValue.Position,DEC);
    Serial.print(",");
    Serial.print(EncoderValue.Velocity,DEC);
    Serial.print(",");
    Serial.print(CurrentCart.Position,DEC);
    Serial.print(",");
    Serial.print(CurrentCart.Velocity,DEC);
    Serial.print(",");
    Serial.print(CurrentCart.Acceleration,DEC);
    Serial.print(",");
    Serial.print(DesiredCart.Velocity ,DEC);
    Serial.print(",");
    Serial.println("");
