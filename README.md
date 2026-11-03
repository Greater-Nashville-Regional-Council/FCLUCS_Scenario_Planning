# FCLUCS_Scenario_Planning  

G:\3-GitHub\FCLUCS_Scenario_Planning  

This repository contains work preparing for and carrying out the FCLUCS scenario planning.  

What we need: Household Population, Total Employment 

Base Year:  

Tennessee Counties – we have this by county and block from our Land Use model inputs.  

Kentucky Counties – we have already created county controls with the same methodology, and can best almost duplicate the distribution but save some key time and effort in one area because of the lower growth rate in these Kentucky counties than our MidTN counties.  

Household Population KY:  

County Control 2023: The PEP tracks housing units, total population, and group quarters population. We use total population – group quarters population to get household population, and we get the household control total by dividing the household population by average household size as this product doesn’t track vacancy data. So at the county level we have total population, group quarters population, household population, housing units, and households.  

Distribution to the block level: We have households (non-vacant housing units) from the 2020 decennial census. We can use this distribution of the county control to take the household population and households down to the block level. For the Tennessee county inputs to the Land Use model, the team had used real property parcel data to look at new residential buildings as improvements between 2020 and 2023 and adjust that distribution. I believe that the level of effort to source, learn, and clean Kentucky parcel data combined with the low to no growth we’ve seen in Christian and Trigg Counties in those three years doesn’t justify applying a similar adjustment and that we use the 2020 distribution for these 2023 control totals.  

Employment and Employment by Industry KY:  

County Control 2023: Employment and employment by industry baseline methodology is attached (a bit long). The same methodology is applied to Kentucky Counties.
Distribution to block level: 2023 LEHD. We have this for Kentucky Counties as well.  

Scenario BAU 1:  

Tennessee Counties – We have the county controls and block distributions for 2050 from Woods and Poole and our UrbanSIM model.  

Kentucky Counties – We have the county controls from Woods and Poole for 2050. We have decided it’s outside of budget and not necessary to run the entire UrbanSIM model to get the distributions needed for the BAU, and that we will use our internal team and Tetra Tech to produce this.  

*In both cases below, the key is to find the best methodology for the furthest projection of the datapoint we’re looking for and use that to distribute. OR to accept the current distribution plus information from our locals. Or some combination.   

Data Options:
Household Population: We can look at growth to 2030 using the global human settlement layer, which can be allocated to Census blocks, and then use that to growth distribution to spread the Woods and Poole 2050 control totals.  

Employment and Employment by Industry: JobsEQ provides 10-year forecasts at the industry level (NAICS – not BEA) at the block level. We can use that industry growth and small-area distribution we see in JobsEQ as the distribution to spread the Woods and Poole 2050 control totals.  

*The advantage of JobsEQ is that it gives us a uniformly available small-area framework. Some projections are available for select substate and subcounty geographies, but not uniformly like this. JobsEQ gives us an established methodology for producing geographically detailed industry estimates and it allows us to do something besides just uniform growth.  

Scenario BAU 2:  

We have the county controls and block distributions for population 2050 from Woods and Poole and our UrbanSIM model for counties that have not disputed these, and the county input for control totals for other counties (decide if this will vary by jurisdiction– where we can use the block level distribution from our UrbanSIM model to allocate to these alternative controls. We have some input on employment and employment by industry from Montgomery County as well, so we will have to decide if we want to incorporate this into the totals and if this will vary by jurisdiction.  

Recommendations for allocations are the same.
