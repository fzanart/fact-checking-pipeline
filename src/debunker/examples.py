"""
CARDS clamis and rebuttal examples
"""

FALLACY_CLAIMS = {
    "ad hominem": [
        "Climate science is unreliable.",
        "The climate movement is unreliable.",
        "The media is alarmist about climate change.",
        "Politicians are biased about climate change.",
        "Environmentalists are biased.",
        "Scientists are biased",
    ],
    "anecdote": [
        "Cold weather disproves global warming.",
    ],
    "cherry picking": [
        "Arctic is not melting.",
        "Coral reefs have recovered before so they will survive climate change.",  #
        "Ice is not melting.",
        "Greenland is not melting.",
        "Glaciers are not melting",
        "There has been a hiatus in global warming in recent years.",
        "Oceans are cooling.",
        "Sea level rise is exaggerated.",
        "Global warming is caused by the sun.",
        "Climate sensitivity is low due to negative feedbacks.",
        "Renewable technologies harms the environment.",
        "Climate policies will limit peoples' freedoms.",
        "The public do not support for climate action.",
        "Clean energy is unreliable.",
        "It is better to adapt to climate change than to mitigate.",
    ],
    "conspiracy theory": [
        "Governments are secretly conspiring to create climate policy.",
        "Climate scientists are conspiring to deceive the public.",
    ],
    "false choice": [
        "In the past, CO2 lagged warming so CO2 does not cause warming.",
    ],
    "false equivalence": [
        "Extreme weather is not linked to climate change.",
        "Ocean cycles are driving global warming.",
        "Species can adapt to climate change.",
        "Only a few degrees of global warming is insignificant.",
        "Climate policy is too difficult.",
        "Clean energy will not work.",
        "Climate change is a religion.",
    ],
    "impossible expectations": [
        "Antarctica is not melting.",
        "Greenland is not melting.",
        "Climate policies are ineffective at preventing climate change.",
        "A single climate policy would have a negligible impact in reducing climate change.",
        "Green jobs are small and growing slowly.",
        "Climate models are unreliable.",
    ],
    "misrepresentation": [
        "They changed the name from 'global warming' to 'climate change'.",
        "CO2 is a trace gas so can not have a strong effect.",
        "Water vapor is the strongest driver of current global warming.",
        "The tropospheric hot spot has not been observed, disproving human-caused global warming.",
        "Climate proxies are unreliable.",
        "The surface temperature record is unreliable.",
    ],
    "oversimplification": [
        "The greenhouse effect is saturated so adding more CO2 will not make much difference.",
        "Human CO2 emissions are tiny compared to natural CO2 emissions.",
        "Polar bear populations are increasing.",
        "CO2 is plant food.",
        "Climate policy increases costs and are harmful.",
        "Climate policies will limit peoples' freedoms.",
        "Climate action is pointless because of China's emissions.",
        "Solving climate change is too hard.",
        "We need fossil fuel energy.",
        "Fossil fuels are cheap.",
    ],
    "single cause": [
        "Antarctica is not melting.",
        "We are heading into an ice age.",
        "Global warming is caused by natural cycles.",
        "Global warming is caused by the sun.",
        "Climate is changing because climate has always changed.",
    ],
    "slothful induction": [
        "Geological sources are warming the oceans.",
        "Climate change is caused by non-greenhouse gas forcings.",
        "There is no evidence that greenhouse warming is driving climate change.",
        "The tropospheric hot spot has not been observed, disproving human-caused global warming.",
        "Climate policies are harmful.",
        "Green jobs are small and growing slowly.",
        "We need fossil fuel energy.",
        "Fossil fuels are plentiful.",
        "Fossil fuels are cheap.",
        "There is no scientific consensus on human-caused global warming.",
    ],
    "red herring": [
        "CO2 is not a pollutant.",
    ],
}


DEBUNKINGS = {
    "Ice is not melting.": "## FACT: Ice is melting across the planet from the Arctic to Antarctica, with Greenland and Antarctica losing hundreds of billions of tonnes of ice per year and glaciers shrinking at an accelerating rate.\n\
## MYTH: Ice isn't melting.\n\
## FALLACY: This argument relies on cherry picking by focusing only on short-term or regional trends. It also demands impossible expectations by suggesting that ice cannot be growing anywhere if global warming is happening.\n\
## FACT: The fact that ice is melting all over our planet is another line of evidence that global warming is real.",
    "Antarctica is not melting.": "## FACT: Even though Antarctic sea ice was growing between 1980 - 2014, it is clear now that Antarctic sea ice has been in steady decline.\n\
## MYTH: Antarctic sea ice isn't melting.\n\
## FALLACY: This argument demands impossible expectations by suggesting ice cannot be growing at any point in time if global warming is happening. It also assumes temperature is the only factor driving sea ice trends. Sea ice formation is complex, with wind also being a factor impacting its growth or decline.\n\
## FACT: Ice is melting across the planet from the Arctic to Antarctica, another line of evidence that global warming is real.",
    "Greenland is not melting.": "## FACT: Greenland on the whole is losing ice, at a rate of over 2 Mount Everests worth of ice every year.\n\
## MYTH: Greenland isn't melting.\n\
## FALLACY: This argument relies on cherry picking by focusing on one small area where ice may be growing while ignoring the rest of Greenland. It may also demand impossible expectations by suggesting that ice cannot be growing in any part of Greenland if global warming is happening.\n\
## FACT: Ice is melting across the planet from the Arctic to Antarctica, another line of evidence that global warming is real.",
    "Arctic is not melting.": "## FACT: Arctic sea ice is shrinking at an accelerating rate.\n\
## MYTH: Arctic sea ice isn't melting.\n\
## FALLACY: This argument relies on cherry picking, focusing on short-term trends and ignoring the long-term decline in sea ice.\n\
## FACT: Ice is melting across the planet from the Arctic to Antarctica, another line of evidence that global warming is real.",
    "Glaciers are not melting": "## FACT: Overall, glaciers across the globe are shrinking at an accelerating rate, threatening water supplies for millions of people.\n\
## MYTH: Glaciers aren't melting.\n\
## FALLACY: This argument relies on cherry picking by focusing only on growing glaciers and ignoring the vast majority of shrinking glaciers.\n\
## FACT: Ice is melting across the planet from the Arctic to Antarctica, another line of evidence that global warming is real.",
    "We are heading into an ice age.": "## FACT: Warming from greenhouse gas emissions far outweighs any cooling influence from natural factors.\n\
## MYTH: We're heading into an ice age.\n\
## FALLACY: This argument assumes that only natural factors drive global warming when in reality, human activity is the main driver of warming\n\
## FACT: Many lines of evidence indicate warming across the global climate.",
    "Cold weather disproves global warming.": "## FACT: Global warming has made hot days more likely and hotter.\n\
## MYTH: Cold weather disproves global warming.\n\
## FALLACY: This argument relies on anecdotal evidence rather than sound or compelling evidence. It also demands impossible expectations by suggesting that if it's currently cold, then global warming cannot be happening.\n\
## FACT: Many lines of evidence indicate warming across the global climate.",
    "There has been a hiatus in global warming in recent years.": "## FACT: Our planet has continued to build up heat since 1998 - global warming is still happening.\n\
## MYTH: There's been a hiatus in global warming in recent years.\n\
## FALLACY: This argument relies on cherry picking, focusing on short-term trends which are not long enough to make conclusions about long-term climate trends.\n\
## FACT: Many lines of evidence indicate warming across the global climate.",
    "Oceans are cooling.": "## FACT: The oceans build up heat with over 90% of global warming going into the oceans.\n\
## MYTH: Oceans are cooling.\n\
## FALLACY: This argument relies on cherry picking regions where oceans may be cooling, ignoring the majority of the ocean which is warming drastically.\n\
## FACT: Many lines of evidence indicate warming across the global climate.",
    "Sea level rise is exaggerated.": "## FACT: Global sea level rise is accelerating due to increased ice melt and thermal expansion.\n\
## MYTH: Sea level rise is exaggerated.\n\
## FALLACY: This argument relies on ignoring that the rate of sea level rise is increasing so future sea level rise will be faster than current levels.\n\
## FACT: Many lines of evidence indicate warming across the global climate.",
    "Extreme weather is not linked to climate change.": "## FACT: Global warming is increasing the amount of energy in the climate system which is intensifying extreme weather events.\n\
## MYTH: Extreme weather is not linked to climate change.\n\
## FALLACY: This argument assumes that past extreme weather is similar to current conditions. However, global warming is generally making extreme weather more intense and/or frequent. For example, a 1 in 1000 year event is now happening more regularly.\n\
## FACT: Many lines of evidence indicate warming across the global climate.",
    "They changed the name from 'global warming' to 'climate change'.": "## FACT: Global warming and climate change have both been used for decades and are two different phenomena, with global warming being the long-term trend of rising global temperature, and climate change being the change in climates due to global warming.\n\
## MYTH: They changed the name from 'global warming' to 'climate change'.\n\
## FALLACY: This argument relies on misrepresentation as both terms have been used frequently for many decades, and the usage of both terms has increased over the past 40 years.\n\
## FACT: The term climate change has been used by scientists for decades. The Intergovernmental Panel on Climate Change (IPCC)—using the term climate change in its title—was formed in 1988.",
    "Global warming is caused by natural cycles.": "## FACT: Many lines of evidence have found that human-caused CO2 pollution is the main driver of modern global warming, overpowering natural factors.\n\
## MYTH: Global warming is caused by natural cycles.\n\
## FALLACY: This argument assumes that there can only be one cause for global warming. It ignores that there are in fact multiple factors driving global warming, including human greenhouse gas emissions.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "Global warming is caused by the sun.": "## FACT: Changing patterns in the yearly and daily cycle confirm human-caused global warming, rule out the sun.\n\
## MYTH: Global warming is caused by the sun.\n\
## FALLACY: This argument ignores the evidence that the sun has been cooling over the past few decades of global warming. It also assumes that solar activity is the only one driver for global warming, which ignores other factors such as man-made greenhouse gases.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "Geological sources are warming the oceans.": "## FACT: The observed patterns of ocean warming are consistent with being caused by greenhouse warming, and rule out other causes like geological sources.\n\
## MYTH: Geological sources are warming the oceans.\n\
## FALLACY: This argument ignores the fact that ocean warming is coming from the ocean's surface, driven by greenhouse warming.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "Ocean cycles are driving global warming.": "## FACT: The world's oceans are building up heat. This cannot be caused by ocean cycles which merely move heat around, not build up extra heat.\n\
## MYTH: Ocean cycles are driving global warming.\n\
## FALLACY: This argument assumes that short-term temperature change is similar to long-term temperature change, because they both involve temperature change. But they are not equivalent because ocean cycles involve transfer of heat between the ocean and atmosphere while global warming is a planetary build-up in heat.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "Climate is changing because climate has always changed.": "## FACT: While climate has changed naturally in the past, current climate change is faster than past warming events and can only be explained by human activity.\n\
## MYTH: Climate is changing because climate has always changed.\n\
## FALLACY: This argument assumes that what caused climate change in the past (natural factors) must be the same as what's causing climate change now.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "Climate change is caused by non-greenhouse gas forcings.": "## FACT: Human activity has a much greater influence on climate than non-greenhouse gas influences.\n\
## MYTH: Climate change is caused by non-greenhouse gas forcings.\n\
## FALLACY: This argument ignores the body of evidence confirming that burning of fossil fuels is the main driver of global warming.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "There is no evidence that greenhouse warming is driving climate change.": "## FACT: There are many lines of evidence showing that greenhouse gases cause warming and are the main driver of current global warming.\n\
## MYTH: There's no evidence that greenhouse warming is driving climate change.\n\
## FALLACY: This argument ignores the body of evidence confirming that burning of fossil fuels is the main driver of global warming.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "CO2 is a trace gas so can not have a strong effect.": "## FACT: Satellites measure the warming effect from CO2. The increased greenhouse effect is an observed reality.\n\
## MYTH: CO2 is a trace gas so can't have a strong effect.\n\
## FALLACY: This argument misrepresents how CO2 is behaves. Small active substances can have a strong effect (e.g., it only takes a small amount of mercury to poison someone).\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "The greenhouse effect is saturated so adding more CO2 will not make much difference.": "## FACT: Emitting more CO2 means more heat is being trapped high up in the atmosphere where the air is thinner. This is because layers higher up in the atmosphere are less saturated than lower layers.\n\
## MYTH: The greenhouse effect is saturated so adding more CO2 won't make much difference.\n\
## FALLACY: This argument oversimplifies the fact that atmosphere is made up of multiple layers by assuming that CO2 is concentrated in only one layer of the atmosphere.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "In the past, CO2 lagged warming so CO2 does not cause warming.": "## FACT: Ice cores tell us that warming caused the ocean to emit more CO2. Combined with greenhouse effect, this is a reinforcing feedback.\n\
## MYTH: In the past, CO2 lagged warming so CO2 doesn't cause warming.\n\
## FALLACY: This argument is a false choice. While it is true that CO2 causes global warming, that doesn't mean global warming won't also lead to increased atmospheric CO2. CO2 causes warming and warming causes more CO2. The two combined comprise a reinforcing feedback.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "Water vapor is the strongest driver of current global warming.": "## FACT: Water vapour provides a reinforcing feedback, making climate even more sensitive to CO2 emissions.\n\
## MYTH: Water vapor is the strongest driver of current global warming.\n\
## FALLACY: This argument misrepresents water vapor as a climate driver when it is actually a feedback. The amount of vapor in the air depends on air temperature. Warming causes water vapor to rise, which causes further warming: a reinforcing feedback.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "The tropospheric hot spot has not been observed, disproving human-caused global warming.": "## FACT: There are many observed patterns in our climate confirming that greenhouse gases are causing warming.\n\
## MYTH: The tropospheric hot spot hasn't been observed, disproving human-caused global warming.\n\
## FALLACY: This argument ignores new data using the latest, advanced technology that has found a clear signal for the hot spot. It also misrepresents the tropospheric hotspot which is not a fingerprint of anthropogenic warming—it is the result of any type of warming regardless of the cause. Cooling in the stratosphere is a more appropriate fingerprint of anthropogenic warming.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "Human CO2 emissions are tiny compared to natural CO2 emissions.": "## FACT: Humans are emitting billions of tonnes of CO2 into the atmosphere, upsetting the natural balance and raising atmospheric CO2 to levels not seen in millions of years.\n\
## MYTH: Human CO2 emissions are tiny compared to natural CO2 emissions.\n\
## FALLACY: This argument oversimplifies the carbon cycle by ignoring that nature both emits and absorbs CO2, with natural emissions and absorptions being roughly balanced. Human CO2 emissions upset that balance.\n\
## FACT: Many scientific studies have found that human activity is causing global warming.",
    "Climate sensitivity is low due to negative feedbacks.": "## FACT: Independent lines of evidence find that our climate is highly sensitive to CO2 emissions, with reinforcing feedbacks amplifying the initial greenhouse warming from CO2 emissions.\n\
## MYTH: Climate sensitivity is low due to negative feedbacks.\n\
## FALLACY: This argument ignores the many lines of evidence that the net effect of climate feedbacks is strongly positive.\n\
## FACT: Climate change is having negative impacts on society and the environment all over the world, with impacts worsening in the future.",
    "Species can adapt to climate change.": "## FACT: Climate is changing faster than species can adapt to it, causing negative impacts on species all over the world.\n\
## MYTH: Species can adapt to climate change.\n\
## FALLACY: This argument relies on a false equivalence, assuming that current climate change is equivalent to past climate change when what is happening now is unprecedented in millions of years.\n\
## FACT: Climate change is having negative impacts on society and the environment all over the world, with impacts worsening in the future.",
    "Polar bear populations are increasing.": "## FACT: Polar bears need sea ice to hunt, so melting sea ice threatens their survival.\n\
## MYTH: Polar bear populations are increasing.\n\
## FALLACY: This argument oversimplifies the variety of factors that influence polar bear populations. One threat (hunting) has been removed but replaced with an increasing threat (melting sea ice). Polar bears need sea ice to hunt so the shrinking of Arctic sea ice is endangering their populations.\n\
## FACT: Climate change is having negative impacts on society and the environment all over the world, with impacts worsening in the future.",
    "Coral reefs have recovered before so they will survive climate change.": "## FACT: Coral reefs will suffer permanent damage from global warming and ocean acidification.\n\
## MYTH: Coral reefs have recovered before so they'll survive climate change.\n\
## FALLACY: This argument fails to consider that reefs may only be able to recover if there is no new disturbance. Bleaching events will become more frequent with time decreasing this chance of recovery. During past mass extinction events, it took millions of years in the past for coral reefs to recover from mass extinction events.\n\
## FACT: Climate change is having negative impacts on society and the environment all over the world, with impacts worsening in the future.",
    "CO2 is not a pollutant.": "## FACT: A pollutant is any substance that disrupts the environment. Human CO2 emissions have resulted in the disruptive effect of global warming.\n\
## MYTH: CO2 is not a pollutant.\n\
## FALLACY: This argument diverts attention from the issue of global warming by focusing on terminology rather than the negative impacts of climate change. It also misrepresents CO2 as being benign just because it is naturally occurring.\n\
## FACT: Climate change is having negative impacts on society and the environment all over the world, with impacts worsening in the future.",
    "CO2 is plant food.": "## FACT: Plants need the right amount of water to flourish; climate change upsets that balance.\n\
## MYTH: CO2 is plant food.\n\
## FALLACY: This argument oversimplifies the ways that climate change impacts agriculture through increased heat stress and flooding. CO2 fertilisation is just one factor affecting plant growth. The full picture shows that negative impacts outweigh benefits.\n\
## FACT: Climate change is having negative impacts on society and the environment all over the world, with impacts worsening in the future.",
    "Only a few degrees of global warming is insignificant.": "## FACT: At a global scale, a few degrees of warming is a massive amount of heat, causing significant damage to society and the environment.\n\
## MYTH: Only a few degrees of global warming is insignificant.\n\
## FALLACY: This argument is a false equivalence,  assuming two different things—local warming and global warming—are the same.\n\
## FACT: Climate change is having negative impacts on society and the environment all over the world, with impacts worsening in the future.",
    "Climate policies are harmful.": "## FACT: Numerous climate solutions are cheaper than the alternatives before even accounting for the trillions of dollars that will be saved by reducing climate and air pollution.\n\
## MYTH: Climate policies are harmful.\n\
## FALLACY: This argument ignores the impacts on an individual's quality of life when not drastically reducing the fossil fuels. Climate change will lead to a much greater decrease in peoples' quality of life.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Climate policy increases costs and are harmful.": "## FACT: Numerous climate solutions are cheaper than the alternatives before even accounting for the trillions of dollars that will be saved by reducing climate and air pollution.\n\
## MYTH: Climate policy increases costs and are harmful.\n\
## FALLACY: This argument oversimplifying the situation by selectively focusing on the potentially harmful effects of introducing policy while ignoring the harmful effects of taking no climate action.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Renewable technologies harms the environment.": "## FACT: While there may be downsides to any technology, the long-term impacts of taking no climate action are both numerous and severe.\n\
## MYTH: Renewable technologies harms the environment.\n\
## FALLACY: This argument selectively focuses on the negative short-term impacts of clean technologies and ignores the long-term positive effects.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Climate policies will limit peoples' freedoms.": "## FACT: Climate policies are designed to prolong the life of the planet, prolonging our freedom to live and our resources.\n\
## MYTH: Climate policies will limit peoples' freedoms.\n\
## FALLACY: This argument focuses on the negative aspects of regulation while ignoring that regulations are designed to as safeguards to protect people's livelihoods. Furthermore, as climate change worsens, consumer freedoms will become limited as resources become scarce.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Climate policies are ineffective at preventing climate change.": "## FACT: At a global scale, climate change policies are effective in significantly reducing greenhouse gas emissions.\n\
## MYTH: Climate policies are ineffective at preventing climate change.\n\
## FALLACY: This argument demands the impossible expectation that climate policies be perfect or singlehandedly solve climate change. While it is important to ensure a policy is thorough and limits unintended consequences, the consequences will be far worse if we do nothing.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Green jobs are small and growing slowly.": "## FACT: Green jobs are growing steadily. With more development and investment in a sector or with steady growth, green jobs will show accelerating growth in the future.\n\
## MYTH: Green jobs are small and growing slowly.\n\
## FALLACY: This argument falsely assumes that the current growth rate of green jobs will stay the same. Exponential growth always shows slow growth in the early stages.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "A single climate policy would have a negligible impact in reducing climate change.": "## FACT: If every nation agreed to limit CO2 emissions, significant global emissions cuts can be accomplished.\n\
## MYTH: A single climate policy would have a negligible impact in reducing climate change.\n\
## FALLACY: This argument demands impossible expectations by assuming a policy is only worth implementing if it is single-handedly 100% effective in solving climate change.\n\
## FACT: A single policy cannot single handedly solve climate change. We need a suite of policies from all countries in the world in order to solve climate change.",
    "It is better to adapt to climate change than to mitigate.": "## FACT: Failing to mitigate against climate change means that adapting to it will be much harder, as well as more expensive.\n\
## MYTH: It's better to adapt to climate change than to mitigate.\n\
## FALLACY: This argument cherry picks by only looking at the negative economic impacts of climate action while ignoring the benefits. It ignores that failing to mitigate against climate change will also make adapting to climate change more difficult as well as cause economic damage.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Climate action is pointless because of China's emissions.": "## FACT: Solving climate change requires all the world's countries working together to substantially reduce global emissions.\n\
## MYTH: Climate action is pointless because of China's emissions.\n\
## FALLACY: This argument oversimplifies by not recognising that each country has it's different resources, societal challenges, and historical emissions. Developing countries have a right to attain the same standard of living as developed countries, who historically have been emitting CO2 at greater rates.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Solving climate change is too hard.": "## FACT: Climate action can be implemented on all levels of government, through corporations and wider society.\n\
## MYTH: Solving climate change is too hard.\n\
## FALLACY: This argument oversimplifies the situation, arguing that because political agreement can be challenging, it is impossible to implement policies.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Climate policy is too difficult.": "## FACT: Not implementing policy now will make mitigating climate change in the future much harder.\n\
## MYTH: Climate policy is too difficult.\n\
## FALLACY: This argument falsely assumes that global agreement is impossible because it has been difficult before. This in turn may create a self full-filling prophecy about reaching a global climate agreement, as the pessimism makes the task even more challenging to achieve.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "The public do not support for climate action.": "## FACT: While some of the public may be confused about aspects of climate change, public support for climate solutions has been growing.\n\
## MYTH: The public don't support for climate action.\n\
## FALLACY: Often this argument relies on cherry picked data by sampling members of the public who are confused or dismissive about climate change.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Clean energy will not work.": "## FACT: While renewable energy only supply a small part of our power now, technological improvements mean that we will be able to rely on it in the future.\n\
## MYTH: Clean energy won't work.\n\
## FALLACY: This argument falsely assumes that the current situation with renewables will stay the same in the future.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Clean energy is unreliable.": "## FACT: The benefits of clean energy sources far outweigh any unreliable or negative aspects associated with them.\n\
## MYTH: Clean energy is unreliable.\n\
## FALLACY: This argument relies on cherry picking by focusing on negative aspects of renewable energy while ignoring the benefits.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "We need fossil fuel energy.": "## FACT: While fossil fuels have helped us build a successful economy in the past, it assumes that they are the only way to build wealth into the future.\n\
## MYTH: We need fossil fuel energy.\n\
## FALLACY: This argument oversimplifies by ignoring that we don't only need energy but also other resources to sustain livelihoods, which are damaged by the use of fossil fuels. It may also ignore the benefits of switching to renewables in the long run as fossil fuels will inevitably run out.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Fossil fuels are plentiful.": "## FACT: Fossil fuels are not a renewable energy source. We only have a few decades left of fossil fuel use until they run out.\n\
## MYTH: Fossil fuels are plentiful.\n\
## FALLACY: This argument ignores the environmental impacts that comes with burning the remaining fossil fuel reserviors. Even if fossil fuels are not on the brink of running out, there are other reasons we should not use all the remaining fossil fuel reserves. Just because we have fossil fuel doesn't mean we should burn it. It also ignores the benefits of clean energy which not only mitigate climate impacts but are also becoming more affordable and viable.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Fossil fuels are cheap.": "## FACT: While fossil fuels have had a low market price, externalities such as air pollution and adverse health impacts raise the true price on society to be much higher than renewable sources of energy.\n\
## MYTH: Fossil fuels are cheap.\n\
## FALLACY: This argument oversimplifies by ignoring that there is more to energy sources than just cost. Costs through climate impacts should be considered. It also ignores relevant evidence that renewables are reducing in cost and in many cases, becoming even cheaper than fossil fuels.\n\
## FACT: Climate policy is necessary to avoid the worst impacts of climate change, which will have devastating effects on society and the environment.",
    "Climate science is unreliable.": "## FACT: Decades of scientific research, replicated using independent methods, have consistently found that climate change is happening and is caused by human activity.\n\
## MYTH: Climate science is unreliable.\n\
## FALLACY: This argument relies on attacking scientists and science rather than addressing the scientific content itself.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "There is no scientific consensus on human-caused global warming.": "## FACT: A number of scientific studies have found that between 90% to 100% of climate scientists agree that humans are causing global warming, with multipe studies converging on 97% consensus.\n\
## MYTH: There's no scientific consensus on human-caused global warming.\n\
## FALLACY: This argument ignores the many independent lines of evidence that give us confidence in our understanding of climate change.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "Climate proxies are unreliable.": "## FACT: Scientists know how to account for other environmental factors that may affect the proxy data to identify clear trends.\n\
## MYTH: Climate proxies are unreliable.\n\
## FALLACY: This argument misrepresents how climate proxies work. Adjusting measurements is a standard scientific process and necessary to ensure observations accurately reflect reality.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "The surface temperature record is unreliable.": "## FACT: We measure temperature in many ways and all the indicators consistently find that our planet is warming.\n\
## MYTH: The surface temperature record is unreliable.\n\
## FALLACY: This argument misrepresents the situation, as scientists take into account potential urban contamination of the temperature record.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "Climate models are unreliable.": "## FACT: Climate models have made a number of successful predictions based on fundamental physical principles.\n\
## MYTH: Climate models are unreliable.\n\
## FALLACY: This argument demands impossible expectations from climate models, whose projections are averaged over time to reflect long-term externally-forced changes, smoothing out short-term variability like ocean cycles or volcanic eruptions. It's impossible to expect that the two will exactly match.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "The climate movement is unreliable.": "## FACT: Our scientific understanding of climate change is based on many lines of empirical evidence.\n\
## MYTH: The climate movement is unreliable.\n\
## FALLACY: This argument relies on attacking scientists and science to distract from the robust body of evidence that find that human-caused climate change is happening.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "Climate change is a religion.": "## FACT: Climate science is evidence-based whilst religion is faith-based.\n\
## MYTH: Climate change is a religion.\n\
## FALLACY: This argument is a false equivalence, with a superficial comparison between the climate change movement and religion. Climate science is evidence-based while religion is faith-based—the two are distinctly different.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "The media is alarmist about climate change.": "## FACT: Reporting on evidence-based climate science is not biased, but rather a reflection of the scientific consensus about climate change. \n\
## MYTH: The media is alarmist about climate change.\n\
## FALLACY: This argument is an ad hominem attack on the media for their choices to distract from the problem and the evidence.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "Politicians are biased about climate change.": "## FACT: While politicians inevitably have political biases, supporting evidence-based scientific research is not biased or partisan.\n\
## MYTH: Politicians are biased about climate change.\n\
## FALLACY: This argument relies on ad hominem attacks on governments and politicians rather than addresses their arguments or policies.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "Environmentalists are biased.": "## FACT: While environmentalists may have political biases, supporting evidence-based scientific research is not biased or partisan.\n\
## MYTH: Environmentalists are biased.\n\
## FALLACY: This argument relies on ad hominem attacks on environmentalists rather than addresses their arguments or policies.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "Scientists are biased": "## FACT: Our understanding of climate science is supported by many scientists across the world employing independent methodologies to come to robust, consistent conclusions.\n\
## MYTH: Scientists are biased\n\
## FALLACY: This argument relies on attacking scientists instead of engaging with their scientific research.\n\
## FACT: Our understanding of climate change is based on a global community of scientific experts collecting and analysing evidence that point consistently to the reality of human-caused global warming.",
    "Governments are secretly conspiring to create climate policy.": "## FACT: Many countries have open and transparent processes for developing and implementing climate policies. Governments and corporations are subject to freedom of information laws, which means that citizens can request access to documents and records related to climate policy. This transparency makes it difficult to hide any nefarious activity.\n\
## MYTH: Governments are secretly conspiring to create climate policy.\n\
## FALLACY: This argument is a conspiracy theory, arguing that governments are working with evil intent.\n\
## FACT: The claim that climate policy is part of a secret conspiracy is not supported by evidence. There are more plausible explanations for the actions of governing bodies and corporations. The overwhelming scientific consensus on climate change provides strong reasons for taking action to address this global challenge.",
    "Climate scientists are conspiring to deceive the public.": "## FACT: Scientific research is inherently open and transparent. Researchers publish their findings in peer-reviewed journals, allowing other scientists to examine their methods and data. Scientific findings are only considered valid if they can be replicated by other researchers. This process of scrutiny helps to ensure the reliability of scientific knowledge.\n\
## MYTH: Climate scientists are conspiring to deceive the public.\n\
## FALLACY: This argument is a conspiracy theory, arguing that scientists are secretly plotting with evil intent.\n\
## FACT: The claim that scientists are engaged in a conspiracy to suppress dissenting views is not supported by evidence. The scientific process is inherently open, transparent, and self-correcting.",
}
