# Covid-19_model
New covid-19 model.

> Based on the SIR model, but with additions of:
>  
>  - Delays
>  - Deaths 
>  - Variable transmission rate, dependent from government action U
> 
> State Variables:
> 
>  - S = Subsceptible
>  - I = Infective
>  - R = Removed
>  - D = Death
>  - Pd = Probability of death
>  - Tr = Transmision rate
> 
> constant parameters:
>    
>
>  - a = number of days for the infected to show sintoms
>  - b = number of days for the infected to begin infecting
>  - maxtr = maximum tr, normally before quarantine
>  - mintr = minimum tr, normally when severe quarantine
>  - rr = recovery rate
>  - maxdr = maximum death rate, normally when sanitary system are collapsed
>  - mindr = minimum death rate, normally when the sanitary system is not collapsed.
>  - Icol = Infected rate to collapse the sanitary system.
>  - inf_test = rate of tested from infected.


This model is made on 26 March 2020.
Currently there are around 500,000 cases confirmed globally in 180+ countries.
The data has been collected from the governments and shared globally. 

Few considerations to take in account:
- The collection of the data is different from country to country
- The number of tests made from each country differ
- Few governments may fake the data to their political benefit
- The poblation of tested people differ from country to country
- Each country has their own natural transmission rate, depending on the culture, temperature...etc

To conclude, Is not an easy dataset to work on and extrapolate the value of the parameters of the model.
Anyway, Let's try it.
