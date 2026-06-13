                                                       RESEARCH ARTICLE

                                                       Digital Identity: The effect of trust and
                                                       reputation information on user judgement in
                                                       the Sharing Economy
                                                       Mircea Zloteanu ID1*, Nigel Harvey2, David Tuckett3, Giacomo Livan ID1,4

                                                       1 Department of Computer Science, Faculty of Engineering, University College London, London, United
                                                       Kingdom, 2 Department of Experimental Psychology, Division of Psychology and Language Sciences,
                                                       University College London, London, United Kingdom, 3 Centre for the Study of Decision-Making Uncertainty,
a1111111111                                            University College London, London, United Kingdom, 4 Systemic Risk Centre, London School of Economics
a1111111111                                            and Political Sciences, London, United Kingdom
a1111111111
                                                       * m.zloteanu@ucl.ac.uk
a1111111111
a1111111111

                                                       Abstract
                                                       The Sharing Economy (SE) is a growing ecosystem focusing on peer-to-peer enterprise. In
    OPEN ACCESS                                        the SE the information available to assist individuals (users) in making decisions focuses
Citation: Zloteanu M, Harvey N, Tuckett D, Livan G     predominantly on community-generated trust and reputation information. However, how
(2018) Digital Identity: The effect of trust and       such information impacts user judgement is still being understood. To explore such effects,
reputation information on user judgement in the
                                                       we constructed an artificial SE accommodation platform where we varied the elements
Sharing Economy. PLoS ONE 13(12): e0209071.
https://doi.org/10.1371/journal.pone.0209071           related to hosts’ digital identity, measuring users’ perceptions and decisions to interact.
                                                       Across three studies, we find that trust and reputation information increases not only the
Editor: Jason Anthony Aimone, Baylor University,
UNITED STATES                                          users’ perceived trustworthiness, credibility, and sociability of hosts, but also the propensity
                                                       to rent a private room in their home. This effect is seen when providing users both with com-
Received: March 7, 2018
                                                       plete profiles and profiles with partial user-selected information. Closer investigations reveal
Accepted: November 29, 2018
                                                       that three elements relating to the host’s digital identity are sufficient to produce such posi-
Published: December 13, 2018                           tive perceptions and increased rental decisions, regardless of which three elements are pre-
Copyright: © 2018 Zloteanu et al. This is an open      sented. Our findings have relevant implications for human judgment and privacy in the SE,
access article distributed under the terms of the      and question its current culture of ever increasing information-sharing.
Creative Commons Attribution License, which
permits unrestricted use, distribution, and
reproduction in any medium, provided the original
author and source are credited.

Data Availability Statement: All data files are
available from the Open Science Framework:             Introduction
https://osf.io/ykag6/.
                                                       Background
Funding: Giacomo Livan and Mircea Zloteanu
                                                       The Sharing Economy (SE) describes a growing ecosystem of online platforms devoted to the
acknowledge support from an Engineering and
Physical Sciences Research Council (epsrc.ac.uk)       exchange of goods and services [1–4]. While a precise and encompassing definition of “sharing
Early Career Fellowship in Digital Economy (Grant      economy” is still debated within academia and business [2,5,6], the concept is grounded in
No. EP/N006062/1). The funder had no role in           peer-to-peer (P2P) enterprise, providing individuals with temporary access to the resources of
study design, data collection and analysis, decision   other individuals [7], while using the platforms simply as an exchange mediator [3,8]. In this
to publish, or preparation of the manuscript.
                                                       respect, despite sharing its peer-to-peer nature with other online environments (such as e-
Competing interests: The authors have declared         commerce websites), the SE represents a distinctly unique concept.
that no competing interests exist.




PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                                  1 / 18
                                                                                                                 Digital Identity and user judgment



                                              The SE has seen fantastic growth and high adoption rates among the general population
                                           [5], creating value on an unprecedented scale [3,9], and rivaling well established sectors of the
                                           traditional economy [10]. The types of platforms that have emerged around the SE paradigm
                                           range across all domains and markets, from accommodation (e.g., Airbnb) and taxi services
                                           (e.g., Uber) to household appliances (e.g., Zilok) and clothes (e.g., GirlMeetsDress).


                                           Trust and reputation
                                           In most marketplaces, individuals are aware that the services they request are subject to regula-
                                           tions, consumer protection laws, and monitoring by governmental bodies, ensuring a degree
                                           of liability, security, and safety. Within the SE, such protections are reduced [5], as SE plat-
                                           forms offer direct and largely unmediated interaction between individuals who have never met
                                           before neither offline nor online [1,3]. SE operations require a high level of trust on behalf of
                                           all parties involved [11], which needs to be established on a personal level that goes well
                                           beyond the mere exchange of goods, in the absence of indicators typically employed to signal
                                           quality or reliability in traditional markets. In this respect, trust in the SE differs significantly
                                           from the trust associated to other forms of online economic exchange, such as business-to-
                                           consumer and consumer-to-consumer e-commerce [2,6,12].
                                               In recent years, the role of trust in the online environment has received significant attention
                                           [13–19]. While its precise definitions may vary depending on the context, here trust refers to
                                           the psychological state reflecting the willingness of an actor to place themselves in a vulnerable
                                           situation with respect to the actions/intentions of another actor, in the absence of a direct abil-
                                           ity to monitor or control the other party [20,21]. Thus, trust always involves some aspect of
                                           risk, uncertainty, vulnerability, and the expectation of reciprocation.
                                               By extension, the ability to infer the trustworthiness of the individuals with whom users
                                           wish to engage is fundamental to the SE’s operation [11,22–26]. This process is typically facili-
                                           tated by requiring SE users to establish a digital identity (DI; namely, what the user decides to
                                           share on the platform and the information generated by the community, see the next Section).
                                           Hence, following Todorov and colleagues [27,28], throughout this paper we operationalize
                                           trust in the SE in terms of the perceived trustworthiness of its users, and how this is affected by
                                           the information they share on SE platforms. For the sake of brevity, throughout the paper our
                                           discussions regarding the roles and effects of trust refer to this concept of trustworthiness.
                                               Individuals in the SE (i.e. users), themselves, gravitate towards information relating to the
                                           trustworthiness of the individuals they wish to engage with before deciding to interact [29–31].
                                           Furthermore, research has shown that trust, in turn, has a significant impact on user decision-
                                           making and behavior [13,15,17,32].
                                               Another component driving user behavior within the SE is user reputation. Reputation in
                                           the SE reflects the perception the community has towards a user, through their longevity on a
                                           platform, contributions to the community, and outcome of past engagements (typically, repre-
                                           sented as numeric or valence scores). Reputation can be considered an aggregate representa-
                                           tion of trust towards a certain individual or entity. Thus, in the SE a good reputation can
                                           effectively perform a regulatory role conducive to trust [25,31]. All in all, trust and reputation
                                           can be considered the most valuable commodities within the SE [3,33,34].
                                               Trust and reputation information are relevant due to the implicit information asymmetry
                                           and economic risks of SE platforms, forcing users to rely on such elements to inform their
                                           decision-making [29,33,35,36]. The success of such a market relies on its ability to reduce
                                           uncertainty in its P2P interactions [3]. In such markets, often, the only source that allow people
                                           to infer the credibility of another user is to relying on their digital identify information. Thus,
                                           trust is crucial for turning a user’s uncertainty into a definitive request to use a service [22].



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                    2 / 18
                                                                                                               Digital Identity and user judgment



                                           Digital identity
                                           DI is often used as a blanket term encompassing the overall online footprint of a given entity,
                                           be it an individual or a company. While in general DI is undoubtedly a complex and multiface-
                                           ted concept, in the SE setting it acquires a rather precise meaning, which arises from the inter-
                                           play of the information SE users willingly share and the information their peers share about
                                           their past interactions with them.
                                              At the core of any SE platform are systems that provide reputation building information
                                           [37], which typically aggregate subjective user generated content (UGC) into a reputation
                                           score; this in turn forms the core of a user’s DI on the platform. Most SE platforms actively
                                           promote mechanisms through which users can share information, rate others, and build a rep-
                                           utation on the platform. Such content usually takes the form of numerical (e.g., ratings
                                           between 1 and 5) and text reviews. Each user has to carefully consider the reputation they fos-
                                           ter within the community, ensuring that their identity convinces others that they are trustwor-
                                           thy and would want to interact with them.
                                              Depending on the platform, the above information is typically complemented with more
                                           objective data through which users can signal trust and build relationships [38]. These include,
                                           but are not limited to, identity verification, photos of sellers and their goods, and sellers’ con-
                                           tact information [39]. The combination of these two types of systems acts to reduce the
                                           implicit uncertainty of operating in such markets [20,23,40]. Yet, still little is known about
                                           how SE users incorporate such information into their decision-making processes.


                                           Aims & research questions
                                           The central research question we address is whether DI impacts the perceived trustworthiness
                                           of SE users. In particular, our goal is to investigate whether SE users are able to integrate the
                                           wealth of available information on their peers’ profiles when deciding with whom to interact.
                                           Our initial hypothesis is twofold. On one hand, we hypothesized that SE users are strongly
                                           affected by the presence of trust and reputation information (TRI), leading to changes in their
                                           judgements towards hosts and the services they offer, possibly without even realizing the
                                           strength of such effects. Yet, the literature on decision making [41–44] informs us that people
                                           often are incapable of integrating information from multiple sources, and unwittingly make
                                           decisions based on a limited number of cues (typically two or three). We expect the same phe-
                                           nomenon to take place in the SE as well, i.e., we hypothesized that SE users’ judgments are
                                           unaffected by the increase in the available information shown on their peers’ profiles above a
                                           certain amount.
                                               We tested these hypotheses by designing an artificial accommodation platform, which
                                           allowed us complete control over the type and amount of information displayed to users.
                                           Hypothetical decision-making scenarios allow the experimental investigation of actual deci-
                                           sion-making processes, and findings from them have been generally found to be consistent
                                           with field-collected data [45]. The profiles were generated to resemble accommodation SE
                                           platforms (e.g., Airbnb). Our choice was motivated by the rise of the SE being historically
                                           driven by a handful of companies, Airbnb being the most globally prominent of them. In this
                                           respect, our choice facilitated ecological validity and the participants’ awareness of the experi-
                                           mental context. Over three experiments, individuals (users) were presented with profiles
                                           reflecting hosts wishing to rent a private room in their house. The aim was to understand
                                           whether the TRI available on hosts’ profiles has an effect on users’ decisions to rent a private
                                           room advertised by a host.
                                               Our first study was exploratory and aimed at collecting data of SE users’ choice patterns.
                                           Indeed, Study 1 assessed the effect of providing users with different amounts of host related



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                  3 / 18
                                                                                                               Digital Identity and user judgment



                                           TRI. This contrasted host profiles containing minimal information (akin to those of new users
                                           on a platform), with profiles containing the full information typically seen on such sites, and
                                           with profiles where the information presented was user-selected (allowing for some under-
                                           standing of the users’ underlying thought processes).
                                               The results from Study 1 contributed to corroborate the aforementioned hypotheses, which
                                           were investigated more deeply in the two following studies. Study 2 focused on the importance
                                           of selecting versus being given the information of interest. Finally, in Study 3, the importance
                                           of the type of information users see was addressed. Here, the aim was to uncover whether spe-
                                           cific TRI elements impact user judgements.
                                               Across all three studies several dependent variables were measured. Initially, the partici-
                                           pants provided their rent decision for the room advertised, then rated their confidence in this
                                           judgment. Subsequently, they provided ratings for their perceived trustworthiness, credibility,
                                           and sociability of the hosts advertising each room. This was done in order to assess how differ-
                                           ences in the amount and type of TRI impacted these dimensions. Specifically, we explored
                                           how providing users such information would affect how trustworthy a host appeared, whether
                                           having TRI on the platform would make the information hosts provided seem more credible,
                                           and whether providing user-generated content from past interactions would make the hosts
                                           appear more sociable. This choice was made as SE platforms often brand themselves as envi-
                                           ronments that favor personal interactions in a unique way. Therefore, in our experiments we
                                           introduced TRI elements that, although not always present in real-world SE platforms, were
                                           designed to test differences in those dimensions (see Study 1‘s Stimuli Section).

                                           Study 1
                                           The first study investigated the effect of providing users with different amounts of host-related
                                           TRI, over three conditions: Hidden, Visible, and Reveal. This contrasted host profiles lacking
                                           TRI (Hidden), with full profiles (Visible), and profiles where only partial user-selected infor-
                                           mation was presented (Reveal). The effect of differences in the amount of TRI on user judg-
                                           ments was measured on ratings of host credibility, trust, sociability, rent decisions, and
                                           confidence. It was predicted that the increased amount of information available would impact
                                           users’ perceptions of hosts, resulting in differences in ratings, and decision to rent the private
                                           rooms. Additionally, allowing users to select host TRI would reveal which elements facilitate
                                           decision-making on SE platforms, or at least which elements users believe facilitates their deci-
                                           sions. The utility of the Reveal condition was in observing participant choices directly, pre-
                                           venting various participant response biases, such as responding according to or against what
                                           they surmise the experiment’s goal to be [46].

                                           Methods
                                              Participants and design. A total of 160 participants were recruited online through Ama-
                                           zon’s Mechanical Turk (mTurk; www.mturk.com) in exchange for a flat fee of $1.00. After
                                           deleting incomplete or invalid cases (n = 36) the final data encompassed 124 participants.
                                              Eiteee asd (65 males, 58 females, one undisclosed; MAge = 35.11, SD = 10.52; range: 20–73).
                                           Written (digital) informed consent was obtained from all participants prior to participation.
                                           This study and all procedures used have been ethically reviewed and received ethics approval
                                           from the University College London Research Ethics Committee (CEHP/2015/534).
                                              An independent-samples design was used, with three levels of Profile (Hidden, Visible, and
                                           Reveal). Participants were measured on multiple dependent variables: rent decision, confi-
                                           dence in decision, perceived sociability of host, trustworthiness of the host, and credibility of
                                           information (also, see S1 Text).



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                  4 / 18
                                                                                                                               Digital Identity and user judgment




                                           Fig 1. Example of host profiles in each condition, indicating which elements were visible to users. In the Hidden
                                           condition, only a picture of the host, one of the room, and a minimal description of the latter were present (NB: these
                                           elements were visible in all conditions). In the Visible condition, 7 additional elements were shown to users. In the
                                           Reveal condition, users had to spend tokens to visualize any 3 out of such 7 elements (the profile above already shows
                                           the 3 users-selected elements, with the 4 non-selected elements remaining obscured).
                                           https://doi.org/10.1371/journal.pone.0209071.g001

                                               Stimuli. Typical SE accommodation profiles were created specifically for the purposes of
                                           this experiment, using the Gorilla platform (www.gorilla.sc). These contained the elements
                                           generally featured on such sites, with the addition of two elements. The profiles were described
                                           as representing a “private room” in the host’s house that they wished to rent out to potential
                                           guests (see Fig 1).
                                               The elements were as follows: a photo of the advertised room, a description of the room, a
                                           photo of the host, host verification, two guest reviews, two host reviews, online market reputa-
                                           tion, social media presence, number of reviews, and star rating (for examples, see S2 Text).
                                               Certain factors were controlled in the creation of the profiles. To ensure quality and eco-
                                           logical validity, all elements were created to reflect the general ratings and content observed on
                                           SE platform profiles [4,47]. Two new elements were uniquely created to introduce further digi-
                                           tal identity cues about the hosts: “social media presence” and “online market reputation”. This
                                           decision stems from our perception of SE platform trends towards increased information-
                                           sharing and the role that users’ DI has on their online perception [30].
                                               The former element was introduced, in particular, to gauge its impact on perceived host
                                           sociability (as well as all other trust-related metrics, see S2 Text). Indeed, SE platforms often
                                           market themselves as environments that favor unique personal interactions, which motivated
                                           our choice to introduce an additional TRI element to test sociability.
                                               The latter element, instead, was introduced to assess how cross-platform user reputation
                                           impacts decision-making on other platforms (i.e. the reputation of the user on one P2P plat-
                                           form influencing how they are perceived on another P2P platform). Including this type of
                                           information has been advocated by many, both in the industry and academia (cf. [48]), and in
                                           recent years several startup companies have put forward solutions in this direction. For a com-
                                           prehensive description of element creation and controls implemented see S2 Text.
                                               Procedure. Participants were randomly assigned to one of the three Profile conditions;
                                           Hidden (n = 42), Visible (n = 40), and Reveal (n = 42). They were first given a series of pre-task
                                           questions, including demographics (age, gender, and ethnicity), and SE usage (see S1 Text).
                                           They then received instructions specific to their condition and were provided with an example
                                           profile, familiarizing them with the layout of the profiles, the type of information available,
                                           and the responses they would need to provide.
                                               During the main task, users saw one profile at a time, and were asked if they wanted to
                                           “Rent” or “Not Rent” (binary, forced-choice). The other DV questions were measured on a
                                           10-point Likert-type scale. Confidence was phrased as “How confident are you in your




PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                                     5 / 18
                                                                                                               Digital Identity and user judgment



                                           decision to Rent/Not rent?” (1—Not at all Confident to 10—Very Confident). Sociability was
                                           phrased as “How sociable do you think the host would be?” (1—Not at all Sociable to 10—Very
                                           Sociable). Trustworthiness was phrased as “How would you rate the trustworthiness of the
                                           host?” (1—Very Untrustworthy to 10—Very Trustworthy). While credibility was phrased as
                                           “How credible do you think the information about this room is?” (1—Not at all Credible to
                                           10—Very Credible).
                                               This was repeated over 10 trials. After each trial they were given a “validation” question, to
                                           ensure they were paying attention to the information in the profile. This was in the form of a
                                           question about a specific element on the profile (e.g., “What were the colors of the walls?”,
                                           with an open-ended response). Users who attempted to go back in order to check profiles once
                                           more before answering the validation question were treated as invalid cases and discarded
                                           from the analysis. The elements comprising each profile were randomized between partici-
                                           pants, reducing the artificial influence of specific combination on the responses. The inclusion
                                           of the validation questions in our design was warranted due to the attention benefits such
                                           questions can have on respondents (see [49]). In this respect, our design was in line with well-
                                           established practices for web-based experiments [49]. However, we note that data on user
                                           accuracy on the validation questions was not collected, and thus we cannot make inferences as
                                           to their relationship with user judgements.
                                               In the Hidden condition, users saw a host’s profile with minimal information presented
                                           about a room offered. This was limited to a photo of the room, a picture of the host, and a
                                           description relating to the room; these were always shown regardless of the profile condition.
                                           In the Visible condition, users saw a fully populated host profile, containing all the elements
                                           detailed above. In the Reveal condition, for each profile users had three tokens to “spend” on
                                           revealing any information they desired to help in their judgements. The elements available
                                           were: host verification, guest reviews, host reviews, online market reputation, social media
                                           presence, number of reviews, and star rating. The information regarding the spending of the
                                           three tokens was recorded in each trial. After the main task was completed, participants had to
                                           answer several post-task questions, and were debriefed (see S1 Text).


                                           Results
                                           Users’ ratings were summed across the 10 trials and analyzed on each of the five dependent
                                           measures based on the three Profile conditions.
                                              For decisions to rent the rooms, a one-way analysis of variance (ANOVA) revealed a signifi-
                                           cant main effect of Profile, F(2,121) = 3.44, p = .035, η2 = .054. Post-hoc Tukey’s HSD tests
                                           showed a significantly higher number of rent decisions in the Reveal condition (M = 8.05,
                                           SD = 2.23) than the Hidden condition (M = 6.60, SD = 2.43) and, p = .027. No other compari-
                                           sons were significant.
                                              Confidence in rent decisions was not found to be affected by Profile condition, F < 1, p =
                                           .893, suggesting that the type and amount of information participants saw on the profiles did
                                           not influence their confidence. Overall, the average confidence was very high for rent decisions
                                           (M = 7.58, SD = 1.3 per profile).
                                              Ratings of host sociability were significantly affected by Profile condition, F(2,121) = 6.41,
                                           p = .002 , η2 = .096. Post-hoc tests showed significant lower user ratings for the Hidden condi-
                                           tion (M = 60.81, SD = 16.07) compared to both the Visible (M = 70.83, SD = 13.69), p = .006,
                                           and the Reveal conditions (M = 70.50, SD = 13.56), p = .008.
                                              Similarly, a main effect of host trustworthiness based on Profile was found, F(2,121) = 8.94,
                                           p < .001 , η2 = .129. Post-hoc tests revealed significantly lower ratings in the Hidden condition
                                           (M = 63.50, SD = 15.50) compared to both the Visible (M = 75.13, SD = 14.29), p = .001, and



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                  6 / 18
                                                                                                                 Digital Identity and user judgment



                                           the Reveal (M = 74.36, SD = 12.07) conditions, p = .002. No other significant comparisons
                                           were found.
                                               Finally, a main effect of percevied credibility was found, F(2,121) = 7.00, p < .001 , η2 =
                                           .104. Post-hoc comparisons revealed that the Hidden condition (M = 67.48, SD = 14.64) pro-
                                           duced significantly lower ratings than both the Reveal (M = 76.69, SD = 11.87), p = .005, and
                                           Visible (M = 77.05, SD = 13.04), p = .004, conditions.
                                               As the data suggest a lack of difference in user ratings between the Visible and Reveal condi-
                                           tion, Bayesian independent-samples t-tests were conducted to complement the frequentist
                                           analysis. Considering the null hypothesis of no difference between the two conditions, tenta-
                                           tive results were found in support of this claim. For all measures, the Bayes factor equaled
                                           between BF01 = 2.6–4.34, indicating that the data was around 3 to 4 times more likely under
                                           then null than the alternative hypothesis (S3 Text).
                                               Triplet analysis. To obtain a better understanding of user selection preference for elements
                                           in SE platforms, an analysis of user token “spending” patterns in the Reveal condition was con-
                                           ducted. Each trial from each participant was treated as a unique vector of element selection
                                           from the total seven available items. Thus, the triplets of each of the 42 participants over the 10
                                           trials were analyzed, 420 triplets in total. The triplet selection patterns were compared to a null
                                           model of random selection, using a binomial distribution (for details, see S4 Text).
                                               Initially, with respect to the frequency of observation of certain elements, a few results are
                                           relevant. It was found that 89.5% of the selected triplets featured at least one of the two following
                                           elements: “star ratings” and “guest reviews”. Furthermore, 47.1% of the triplets featured both
                                           items, suggesting a strong user preference towards the two items. When testing for the over-
                                           representation of triplets, we find three combinations to be statistically significant at the 1% uni-
                                           variate level. These are: “star ratings + guest reviews + number of reviews”, “star ratings + guest
                                           reviews + host verification”, or “star ratings + guest reviews + host reviews”. These were inter-
                                           preted as the triplets of TRI information users prefer most to aid in their decision-making.


                                           Discussion
                                           This study finds that providing users with typical SE platform TRI increases their positivity
                                           towards their peers, rating them higher on sociability, trustworthiness, and credibility. Impor-
                                           tantly, this also resulted in an increased number of rent decisions. Differences were observed
                                           when comparing user ratings in the Hidden condition, where all but the basic information was
                                           present, with the Visible and Reveal condition, where reputation and trust information was
                                           provided to varying degrees. The results also suggest that seeing a full profile (Visible) or one
                                           with only partial, but user-selected, information (Reveal) results, on average, in similar judge-
                                           ments towards hosts. Considering the difference in information between the two conditions
                                           (i.e. seven elements in the Visible condition and three user-selected elements in the Reveal
                                           condition), two explanations are proposed.
                                               Potentially, the act of selecting which elements to see impacted users’ perception, leading to
                                           the belief that these elements are the most relevant/useful for their decision [50]. Thus, the act
                                           of selecting specific information may be generating this “positivity effect” (i.e. increased ratings
                                           towards hosts on all measures).
                                               Alternatively, it may be that users rely only on a few elements when making their decisions,
                                           as argued by past decision-making research [50–52]. Thus, users may not be able to incorpo-
                                           rate in their judgment the additional information present in a full profile.
                                               A final noteworthy finding is that confidence in user decision was generally high and was
                                           not affected by the Profile condition. This suggests that the TRI is not a factor that impacts
                                           how confident users are in their SE rental decisions.



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                    7 / 18
                                                                                                               Digital Identity and user judgment



                                           Study 2
                                           Study 2 was devised to unpack the effects relating to the act of selection and the amount of
                                           information on user judgement, as the data indicated that users relying on three selected ele-
                                           ments rated hosts similarly to participants which had access to all seven elements.
                                              People often report using complex strategies and a large number of cues when making their
                                           judgements; however, empirical studies show that they fail to accurately use more than two or
                                           three cues at any one time, and incorrectly predict which ones play a role in their decision-
                                           making process [41,43,44,50,52]. Thus, the lack of difference due to the amount of information
                                           may be explained either by the fact that (1) users considered the elements they selected as
                                           being more informative towards their final decision, leading to equally positive judgements, or
                                           (2) users seeing more than three elements could not incorporate these into their decision-mak-
                                           ing (i.e. discounting information), thus producing no differences in judgement.
                                              A modification of Study 1’s design was implemented. Using the results from the Reveal
                                           condition, we selected element triplets to present to users directly and compared their
                                           responses to users that selected three elements. This ensured that the amount of information
                                           was kept constant (i.e. three pieces of TRI per profile), and that any difference in renting deci-
                                           sion or perceptions of hosts would be a result of the act of selecting information.


                                           Methods
                                              Participants and design. 120 participants were recruited through mTurk, in exchange for
                                           $1.00. After deleting incomplete cases (n = 3), 117 participants remained.
                                              Eiteee asd (65 males, 52 females; MAge = 36.21, SD = 10.35; range: 20–69). The design was
                                           similar to that of Study 1, with Profile having two conditions: 3-Seen, 3-Reveal. Participants
                                           were measured on the same DVs as Study 1.
                                              Stimuli. The profiles in the 3-Seen condition contained only three TRI elements to assist
                                           in user decision-making, selected based on the data from the previous study. In this condition
                                           each profile contained one of the three triplet combinations whose selection frequency was
                                           found to be significant in Study 1: “stars + guest reviews + number of reviews”, “stars + guest
                                           reviews + host verification”, or “stars + guest reviews + host reviews”. In the 3-Reveal condi-
                                           tion, the same profile generation procedure as in Study 1’s Reveal condition was employed.
                                           This allowed for a direct comparison of the effect of choice on user judgement, as information
                                           was kept constant in all conditions.
                                              Procedure. The procedure was identical to that of Study 1, but here participants were ran-
                                           domly assigned to one of the two Profile conditions: 3-Seen (n = 61) or 3-Reveal (n = 56).
                                           Within the 3-Seen condition, participants were further randomly divided into the three sub-
                                           conditions, based on the triplet they saw. Thus, each participant in the 3-Seen sub-condition
                                           saw a specific triplet throughout his/her trials (randomized between participants with a rate of
                                           1/3). In all conditions participants saw 10 profiles and responded to questions regarding each
                                           profile using the same scales as Study 1. A control was also placed on the experiment which
                                           prevented participants from double-checking profiles after seeing the validation questions.


                                           Results
                                           Multiple independent samples t-tests were conducted to compare the responses in the 3-Seen
                                           and 3-Reveal conditions for each DV. The data revealed no significant differences in any of the
                                           responses users gave based on Profile condition, on any of the measured variables, ts � 1, ps >
                                           .05. This supports the explanation that users do not rely on more than three pieces of informa-
                                           tion judging a host’s profile (for additional analyses, see S5 Text).



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                  8 / 18
                                                                                                               Digital Identity and user judgment



                                              To provide more support, Bayesian independent-samples t-tests were conducted on the
                                           data, which did favor this conclusion. Moderate to substantial support in favor of accepting
                                           the null of no difference between the 3-Seen and 3-Reveal conditions was found, BF01 between
                                           2.29 and 3.77 for all DVs (S5 Text).


                                           Discussion
                                           The data suggests that users are not affected by the act of selecting which TRI they want to see
                                           before making a rental decision beyond simply being presented three pieces of information.
                                           On all measured variables, users provided similar responses in the 3-Seen and 3-Reveal condi-
                                           tions. This suggests that users’ judgements are influenced by seeing at least three elements of
                                           TRI, but are unaffected by either the act of selecting said information or seeing more than
                                           three (S5 Text).


                                           Study 3
                                           People find uncertainty unpleasant and seek to reduce it [53]. Relying on information pro-
                                           vided by others may assist with this issue, allowing users to reduce the number of alternatives
                                           and task complexity [54]. However, the results from the above studies raise questions about
                                           the actual usefulness to users of the information available on SE platforms.
                                              Is the information in the elements presented to users impacting decisions, or do users sim-
                                           ply need three elements to believe they are making an “informed” decision? To understand
                                           this, the third study assessed whether specific triplets result in differences in users’ judgements
                                           about hosts’ credibility, sociability, trustworthiness, and decision to rent a room. Here, users
                                           saw one of three options. From Study 1’s Reveal condition, specific triplets were chosen to
                                           reflect the least selected triplet combinations (3-Avoided), the three most selected triplet com-
                                           binations (3-Wanted), and triplets containing a random combination of the remaining ele-
                                           ments (3-Random).
                                              A significant difference in users’ judgements between conditions would support the claim
                                           that users have a preference for what information they use when making their rental decisions,
                                           which in turn affect their ratings of hosts. Alternatively, a lack of a difference would suggest
                                           that users simply require the presence of three elements for the positivity effect to occur.


                                           Methods
                                              Participants and design. 189 participants (103 males, 86 females; MAge = 34.09,
                                           SD = 10.23; range: 19–48) were recruited through mTurk, in exchange for $1.00. The design
                                           was similar to the previous studies, with Profile having three conditions: 3-Wanted, 3-Avoided,
                                           3-Random. Participants were measured on the same DVs as the previous studies.
                                              Stimuli. In the 3-Wanted condition, profiles were generated using the same three triplet
                                           combinations as in Study 2’s 3-Seen condition. In the 3-Avoided condition, profiles were com-
                                           prised of three triplet combinations chosen so as to be the least selected combinations by users
                                           in Study 1’s Reveal condition (see S4 Text). In these sub-conditions, “host verification” and
                                           “host reviews” were always shown together, while the third element was either “social media
                                           presence”, “online market reputation”, or “number of reviews”. In the 3-Random condition,
                                           profiles were comprised of randomly selected triplet combinations formed from the remaining
                                           unused combinations.
                                              Procedure. Participants were randomly allocated to one of the three Profile conditions:
                                           3-Wanted (n = 67), 3-Avoided (n = 67), 3-Random (n = 55). For the 3-Wanted and 3-Avoided
                                           conditions, participants were further divided into their respective three sub-conditions.



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                  9 / 18
                                                                                                                Digital Identity and user judgment



                                           Participants saw 10 host profiles in each condition containing a consistent triplet of informa-
                                           tion throughout. They responded to each profile using the same scales as in the previous
                                           studies.


                                           Results
                                           Multiple one-way ANOVAs were conducted to uncover any differences in users’ judgments
                                           based on Profile condition. The data did not reveal any statistically significant effects of Profile
                                           on any of the measured variables, Fs < 1, ps > .44 (for additional analyses, see S6 Text).
                                              To provide additional support for the findings of no differences in user judgments based on
                                           specific elements, the frequentist analyses were complemented with a Bayesian approach. Test-
                                           ing the assumption of no difference from the null hypothesis, the Bayesian ANOVA conducted
                                           on rent decisions between the three Profile conditions revealed a Bayes factor of BF01 = 9.05,
                                           indicating that the data was around 9 times more likely under the null than the alternative
                                           hypothesis. For confidence, a BF01 = 13.35 was found in favor of the null. With regards to host
                                           ratings, for sociability a BF01 = 14.36 was found, for trustworthiness a BF01 = 14.01 was found,
                                           and for credibility a BF01 = 12.15 was found.


                                           Discussion
                                           The data consistently shows that the information contained in the individual TRI elements
                                           does not influence judgment beyond their simple presence. No differences in user judgements
                                           were found when comparing triplets that users selected most often (3-Wanted), or the ones
                                           they avoided selecting (3-Avoided), or simply showing three random elements (3-Random).
                                           The findings suggest that providing users with at least three TRI elements to aid their deci-
                                           sion-making is sufficient to produce a strong positivity in their judgements of hosts on SE
                                           accommodation-style platforms.


                                           General discussion
                                           The SE’s proliferation brings opportunities for individuals, but also potential, and yet
                                           unknown, risks. The information individuals rely on in SE platforms differs significantly from
                                           what consumers generally rely on in traditional marketplaces. Namely, there is an overreliance
                                           on UGC to assess the trustworthiness and reputation of other users. In this respect, the novelty
                                           of the SE and its multiple platforms raises many questions regarding people’s judgments and
                                           their ability to use such information to make informed decisions.
                                               To understand the impact of trust and reputation based systems on human judgment, the
                                           current paper investigated the role of DI information on user judgments in an artificial SE
                                           accommodation platform. Over three studies, the data showed that users are strongly influ-
                                           enced by the presence of TRI, resulting in an overall positivity towards hosts and increased
                                           tendency to rent rooms. The ratings users gave to hosts on measures of sociability, credibility,
                                           and trustworthiness increased significantly when they were provided information relating to
                                           the hosts’ DI, compared to seeing a profile lacking such information. However, the amount or
                                           specificity of this information did not seem to impact judgement.
                                               The findings of Study 1 speak to the effects that P2P platforms have on people’s decision-
                                           making process. In line with past research, TRI is found to have a significant impact on users’
                                           decision to engage with others on P2P platforms, and to seek their services [30]. Here, we find
                                           that even when maintaining the quality of the service or product constant (i.e. the rooms),
                                           users perceive these in a more positive light if they are provided with TRI regarding the pro-
                                           vider (i.e. host).



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                  10 / 18
                                                                                                                Digital Identity and user judgment



                                               The sharp contrast in rent decisions between the Hidden and other profile conditions
                                           would suggest that TRI is used in deciding not only our perceptions of other peers on SE plat-
                                           forms, but also of the likelihood we will use their goods or services. Viewing the Hidden condi-
                                           tion profiles as reflecting new users on a platform, illustrates that even profiles devoid of TRI
                                           can have success (as seen by the overall high rent decisions). However, it is clear that profiles
                                           containing platform- and community-generated information have a significant advantage
                                           [31,37,40]. Interestingly, though, we found cross-platform reputation not to be a frequently
                                           selected item in the Reveal condition, which suggests that users retain a preference for infor-
                                           mation generated “locally” by the community of the platform of interest. Furthermore, the
                                           lack of a statistically significant difference between the Visible and Reveal conditions implied
                                           either that users were discounting the extra information, resulting in no added positivity
                                           beyond that seen in the Reveal condition, or that the act of selecting which information to
                                           reveal compensated for the information difference.
                                               Study 2 examined these explanations. Here, the data suggested that simply seeing three ele-
                                           ments is sufficient to generate an overall positivity towards hosts and to increase rental deci-
                                           sions, while the act of self-selecting information has no effect on judgment.
                                               Study 3 investigated whether specific information mattered towards this positivity; that is,
                                           whether different elements result in a different perceptions of hosts. Overall, the data strongly
                                           showed that specific combinations did not matter. Irrespective of the frequency with which
                                           users tend to select them naturally, presenting three TRI elements is sufficient to positively
                                           impact judgments and increase rent decisions.
                                               The above findings resonate with the judgment and decision-making literature, expanding
                                           it to online user behavior. From this literature, we know that people are cognitive misers [55],
                                           rarely able to incorporate diverse information from multiple sources into their judgements.
                                           People are also subject to several biases that can influence their perception and the trust they
                                           place in others, as well as the risks they are willing to take. Rather than relying on rational and
                                           strategic process to make decisions, people tend to rely on quick and automatic rules-of-
                                           thumb to make their judgments [42]. Moreover, people are poor at estimating their own pref-
                                           erences for information [43], and are limited to around three cues when making judgments
                                           [44].
                                               Thus, while people show a strong selection preference for specific TRI elements in SE envi-
                                           ronments, these may not reflect specific differences in how the information is perceived or
                                           used by individuals. Indeed, even in novel environments, where people have minimal informa-
                                           tion on how different information affects outcome, they seem to develop strong preferences
                                           over time (see coherent arbitrariness [56]). They may, nonetheless, prefer TRI due to social
                                           convention (i.e. they use it because others seem to use it [57] or because they are accustomed
                                           to relying on it [58]).
                                               Lastly, the literature argues that TRI serves to reduce the uncertainty experienced in SE
                                           environments [3,40]. However, across all studies users’ decision confidence was found to be
                                           stable and overall high, regardless of the amount or type of TRI presented. The data favors our
                                           interpretation that TRI produces a “positivity effect” on user judgement, rather than an
                                           “uncertainty-reduction effect” (cf. [59]).
                                               As a possible limitation to our findings and their implications (see next Section), it is worth-
                                           while to remember that our research was an initial exploration into user judgment in the SE.
                                           In order to minimize spurious effects from extraneous variables a number of controls, detailed
                                           in the Methods Sections, were implemented in constructing our SE platform, while still main-
                                           taining ecological validity with respect to its real-world counterparts. Yet, it can be argued that
                                           our study used incentives that were hypothetical (i.e., lower than those in real-life) rather than
                                           salient (i.e., comparable to those in real life). Is this likely to have mattered?



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                  11 / 18
                                                                                                                 Digital Identity and user judgment



                                              Within the literature on human judgment (across multiple fields; psychology, decision-mak-
                                           ing, economics, etc.) the role of stakes (or motivation/incentive/rewards) has been found to be
                                           rather complex. For instance, Camerer and Hogarth [60] reviewed 74 studies where incentives
                                           were manipulated. The modal finding of their analysis was that incentives had no effect on mean
                                           performance but affected performance variance instead. In 15 of the studies, there was no perfor-
                                           mance standard but, in eight of them, higher incentives made participants more risk-averse. Holt
                                           and Laury [61] similarly showed how the same task can result in different decision-making behav-
                                           ior based on the stakes surrounding the task. In cases with performance standards, Camerer and
                                           Hogarth found very mixed evidence: 27 studies showed no effect of incentives, 23 showed they
                                           facilitated performance, and nine showed they impaired performance. Incentives helped when
                                           better performance could be achieved by applying greater effort: such tasks include those that
                                           involve memory recall (e.g., Kahneman & Peavler, [62]), binary choice, easy problem solving, and
                                           simple clerical tasks. Conversely, incentives can have a detrimental effect on complex tasks (as
                                           demonstrated by research on “choking under pressure”). Financial incentives also have no effect
                                           when a task is very easy to perform well (ceiling effects), when it is very hard to improve perfor-
                                           mance (floor effects), and when the intrinsic rewards from participating in the task are already
                                           high. Many sequential bargaining and game-theoretical tasks come into these categories.
                                              This begs the question: which category does our study fall within? If we consider the study
                                           to be without a performance standard, the research mentioned above suggests that people
                                           would be more risk-averse in their choices if they were more consequential (as in a real-life
                                           scenario). However, we have no way of determining whether our participants were making
                                           risk-seeking choices in the first place. If we consider a higher selection of properties offered by
                                           more trustworthy hosts as an indication of higher performance, it is unlikely on the basis of
                                           Camerer and Hogarth’s [60] conclusions that higher incentives would have changed this. Our
                                           task was complex, but it did not involve memory, and while participating in it provided some
                                           intrinsic rewards, participants were not rewarded/penalized based on outcome.


                                           Implications
                                           Decision-making in an online P2P environment can be a complex task. This process is com-
                                           pounded by issues with the information provided to users to aid in their decision-making that
                                           exist in the SE, two central ones being the overall positivity of such information and, consequently,
                                           its low diagnosticity [4,25]. Indeed, ratings on SE platforms show a stronger bias towards high rat-
                                           ings than on other P2P platforms [4,47], which severely reduces their usefulness to users.
                                               Despite this, there is a trend for increased UGC on online platforms. Users seem more will-
                                           ing to provide such information, even when private and potentially identifying, and platforms
                                           themselves are incentivizing this type of information-sharing [63]. But, our data show that
                                           more of such information may not assist people in any meaningful way, which in turn suggests
                                           that both platforms and their users gain no benefit from collecting and sharing more informa-
                                           tion than is currently available. However, these considerations do not necessarily imply that
                                           limiting the proliferation of UGC would have no consequence.
                                               First, research finds that users trust UGC more than objective metrics when making their
                                           decisions, and carry more weight in the decision-making process than other forms of informa-
                                           tion [30,64]. This is supported by the current data, finding that users show a preference for
                                           selecting elements that result from the aggregate ratings or other users’ testimonials (e.g., guest
                                           reviews), compared to platform-generated information (e.g., host verification).
                                               Second, attempting to reduce the amount of TRI from existing or emerging platforms may
                                           backfire in terms of user perception. Users may expect specific information to be present (even
                                           if not used), with its absence leading to more negative appraisals or to avoidance [65].



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                   12 / 18
                                                                                                               Digital Identity and user judgment



                                              Past research has argued that reputation systems and user-generated reviews may have the
                                           primary purpose of allowing users to learn more about each other before engaging in any
                                           interactions or transactions, acting as a monitoring and policing system [5,66,67]. However,
                                           the current findings demonstrate that this information can also act as a strong influencer in
                                           the perceptions of others, leading users to see peers in a more positive light.
                                              A consideration that emerges from the current findings relates to the concept of online pri-
                                           vacy and how people construct their digital identity. A culture of information-sharing is form-
                                           ing, under the guise of more informed decision-making, which may force individuals wanting
                                           to participate in these communities to share private and sensitive information without any
                                           benefit to the community or individual decision-making outcomes. The current data show it is
                                           unnecessary for users, beyond a certain point, to provide such information, and may even
                                           prove detrimental in the long run. In this respect, we advise caution in how SE platforms
                                           choose to expand and implement their reputation-based systems.


                                           Future directions
                                           As it has been argued [47], the current “5-for-5” culture in ratings drastically reduces the over-
                                           all diagnosticity of TRI in favor of social cohesion and community participation. This moti-
                                           vated our choice to limit the variance in the TRI shown to users to reflect real-world data (see
                                           S2 Text). Within this specific context our findings show that the presence of some TRI, rather
                                           than certain specific elements, is the main driver in trust between SE users. Future investiga-
                                           tions should attempt to ground these findings in established theoretical models to provide a
                                           wider context and understanding of user psychology. For instance, social exchange theory [68]
                                           and reward motivation theory [69,70] may be useful to shed light on the currently observed—
                                           paradoxical—behavior, according to which SE users overall decrease the information content
                                           and diagnosticity of TRI on platforms, while uncritically relying on its mere presence to make
                                           decisions.
                                               The aim of the current research was not to assess whether specific reputation and trust ele-
                                           ments are useful to discriminate among different options, but rather to understand how the
                                           presence of such information affects user judgement and decision-making in a setting that
                                           closely follows real-world patterns.
                                               A natural extension of the current research is to understand how accurate individuals are at
                                           classifying profiles based on their quality. The current design considered the effect of cue diag-
                                           nosticity to the extent that no one particular element provided specific information to classify
                                           a room as “good” or “bad”, but aimed to reflect the natural distribution seen on SE platforms
                                           [4,47]. However, if the profiles users saw varied more in terms of quality and uncertainty,
                                           would ratings reflect these differences or would they continue to show a positivity effect? Intro-
                                           ducing variability and an element of diagnosticity into the information users see on such pro-
                                           files may provide a more complete image of human behavior in the SE, for example varying
                                           the type of profiles users see or analyzing behavioral patterns of “low-raters” (e.g., hyper-criti-
                                           cal or ‘picky’ users) and “high-raters” (e.g., uncritical or lenient users). Similarly, this can
                                           extend into considering the difference in effect and strength that negative information has on
                                           judgments compared to positive information [71]. This research is currently being
                                           undertaken.
                                               Due to explorative nature of our studies, we did not attempt to synthesize our results into a
                                           trust model along the lines, e.g., of the work by Meyer et al. [20] or more recent developments
                                           in the Internet setting (see, e.g., [72]). Yet, we believe that our work, and the aforementioned
                                           ongoing research, represent an important step towards the development of a trust model for
                                           interactions in the SE.



PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                 13 / 18
                                                                                                              Digital Identity and user judgment



                                              Lastly, our work does not take into account the role of platforms as mediators of trust.
                                           Indeed, it has been shown [12] that trust towards a specific platform correlates positively with
                                           trust between its users. While we deliberately eliminated any explicit reference to real-world
                                           SE platforms (e.g., Airbnb) from our artificial accommodation platform in order to suppress
                                           any possible spurious enhancement in the perceived trustworthiness of hosts, it would be very
                                           interesting to replicate our studies in specific platforms as a way to indirectly measure their
                                           additional impact on trust.

                                           Conclusion
                                           Currently, the effect of TRI on user behavior in the SE was investigated. The focus was on how
                                           presenting users with information about hosts’ DI, in an accommodation SE platform, would
                                           impact their perceptions of hosts and the likelihood of renting their private rooms. Over three
                                           studies, the data consistently shows that users find hosts whose profiles display TRI as more
                                           trustworthy, credible, and sociable. More importantly, they also rent more properties if such
                                           information exists. Despite users showing a consistent and strong preference for specific infor-
                                           mation, they demonstrate this positivity in judgement from seeing any three elements relating
                                           to the hosts’ DI. These findings illustrate how TRI can affect user decision-making, cautioning
                                           people on the risks of relying too heavily on this information. Research should carefully con-
                                           sider how information relating to trust and reputation on SE platforms can impact user
                                           judgement.

                                           Supporting information
                                           S1 Text. Additional measures.
                                           (PDF)
                                           S2 Text. Profile elements.
                                           (PDF)
                                           S3 Text. Study 1 Demographics and supplementary analyses.
                                           (PDF)
                                           S4 Text. Triplet analysis.
                                           (PDF)
                                           S5 Text. Study 2 Demographics and supplementary analyses.
                                           (PDF)
                                           S6 Text. Study 3 Demographics and supplementary analyses.
                                           (PDF)
                                           S7 Text. Data processing ReadMe. Explanation of the data processing used for the three
                                           reported studies and description of variables in the datasets.
                                           (PDF)


                                           Acknowledgments
                                           Giacomo Livan and Mircea Zloteanu acknowledge support from an EPSRC Early Career Fel-
                                           lowship in Digital Economy (Grant No. EP/N006062/1).

                                           Author Contributions
                                           Conceptualization: Mircea Zloteanu, Nigel Harvey, David Tuckett, Giacomo Livan.




PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                14 / 18
                                                                                                                        Digital Identity and user judgment



                                           Data curation: Mircea Zloteanu.
                                           Formal analysis: Mircea Zloteanu, Giacomo Livan.
                                           Funding acquisition: Giacomo Livan.
                                           Investigation: Mircea Zloteanu.
                                           Methodology: Mircea Zloteanu.
                                           Project administration: Mircea Zloteanu, Giacomo Livan.
                                           Supervision: Giacomo Livan.
                                           Writing – original draft: Mircea Zloteanu.
                                           Writing – review & editing: Mircea Zloteanu, Nigel Harvey, David Tuckett, Giacomo Livan.



                                           References
                                            1.   Lessig L. Remix: Making art and commerce thrive in the hybrid economy. Penguin; 2008.
                                            2.   Hawlitschek F, Teubner T, Adam MTP, Borchers NS, Möhlmann M, Weinhardt C. Trust in the sharing
                                                 economy: An experimental framework. 2016 International Conference on Information Systems, ICIS
                                                 2016. 2016. Available: https://www.scopus.com/inward/record.uri?eid=2-s2.0-
                                                 85019453377&partnerID=40&md5=078cfb694febff08b8440bca530a48e5
                                            3.   Botsman R, Rogers R. What’s Mine Is Yours: The Rise of Collaborative Consumption. London, UK:
                                                 HarperCollins; 2010.
                                            4.   Zervas G, Proserpio D, Byers J. A first look at online reputation on Airbnb, where every stay is above
                                                 average. 2015; Available: https://ssrn.com/abstract=2554500
                                            5.   Cohen M, Sundararajan A. Self-Regulation and Innovation in the Peer-to-Peer Sharing Economy. Univ
                                                 Chic Law Rev Dialogue. 2015; 82: 116–133.
                                            6.   Hawlitschek F, Teubner T, Gimpel H. Understanding the Sharing Economy—Drivers and Impediments
                                                 for Participation in Peer-to-Peer Rental. IEEE; 2016. pp. 4782–4791. https://doi.org/10.1109/HICSS.
                                                 2016.593
                                            7.   Fraiberger SP, Sundararajan A. Peer-to-Peer Rental Markets in the Sharing Economy. NYU Stern Sch
                                                 Bus Res Pap. 2017; http://dx.doi.org/10.2139/ssrn.2574337
                                            8.   Sundararajan A. Peer-to-peer businesses and the sharing (collaborative) economy: Overview, economic
                                                 effects and regulatory issues. Writ Testimony Hear Titled Power Connect Peer Peer Businesses. 2014;
                                            9.   Yaraghi N, Ravi S. The Current and Future State of the Sharing Economy. Brook India IMPACT Ser.
                                                 2017; No 032017.
                                           10.   Zervas G, Proserpio D, Byers J. The Rise of the Sharing Economy: Estimating the Impact of Airbnb on
                                                 the Hotel Industry. J Mark Res. 2017; 54: 687–705. https://doi.org/10.1509/jmr.15.0204
                                           11.   Belk R. Sharing. John Deighton, editor. J Consum Res. 2010; 36: 715–734. https://doi.org/10.1086/
                                                 612649
                                           12.   Möhlmann M. Digital Trust and Peer-to-Peer Collaborative Consumption Platforms: A Mediation Analy-
                                                 sis. Available SSRN 2813367. 2016; http://dx.doi.org/10.2139/ssrn.2813367
                                           13.   Bart Y, Shankar V, Sultan F, Urban GL. Are the Drivers and Role of Online Trust the Same for All Web
                                                 Sites and Consumers? A Large-Scale Exploratory Empirical Study. J Mark. 2005; 69: 133–152. https://
                                                 doi.org/10.1509/jmkg.2005.69.4.133
                                           14.   Briggs P, Burford B, Angeli AD, Lynch P. Trust in Online Advice. Soc Sci Comput Rev. 2002; 20: 321–
                                                 332. https://doi.org/10.1177/089443930202000309
                                           15.   Flavián C, Guinalı́u M, Gurrea R. The role played by perceived usability, satisfaction and consumer
                                                 trust on website loyalty. Inf Manage. 2006; 43: 1–14. https://doi.org/10.1016/j.im.2005.01.002
                                           16.   Gefen D. E-commerce: The role of familiarity and trust. Omega Int J Manag Sci. 2000; 28: 725–737.
                                                 https://doi.org/10.1016/S0305-04830000021-9
                                           17.   Jarvenpaa S, Tractinsky N, Saarinen L. Consumer Trust in an Internet Store: A Cross-Cultural Valida-
                                                 tion. J Comput-Mediat Commun. 1999; 5: 0–0. https://doi.org/10.1111/j.1083-6101.1999.tb00337.x
                                           18.   McKnight DH, Chervany NL. Conceptualizing trust: a typology and e-commerce customer relationships
                                                 model. Proceedings of the 34th Annual Hawaii International Conference on System Sciences. 2001. p.
                                                 10. https://doi.org/10.1109/HICSS.2001.927053




PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                          15 / 18
                                                                                                                         Digital Identity and user judgment



                                           19.   Wang YD, Emurian HH. An overview of online trust: Concepts, elements, and implications. Comput
                                                 Hum Behav. 2005; 21: 105–125. https://doi.org/10.1016/j.chb.2003.11.008
                                           20.   Mayer RC, Davis JH, Schoorman FD. An Integrative Model of Organizational Trust. Acad Manage Rev.
                                                 1995; 20: 709–734. https://doi.org/10.2307/258792
                                           21.   Rousseau DM, Sitkin SB, Burt RS, Camerer C. Not So Different After All: A Cross-Discipline View Of
                                                 Trust. Acad Manage Rev. 1998; 23: 393–404. https://doi.org/10.5465/AMR.1998.926617
                                           22.   Hawlitschek F, Teubner T, Weinhardt C. Trust in the Sharing Economy. Unternehm–Swiss J Bus Res
                                                 Pract. 2016; 70: 26–44. https://doi.org/10.5771/0042-059x-2016-1-26
                                           23.   Lamberton CP, Rose RL. When Is Ours Better Than Mine? A Framework for Understanding and Alter-
                                                 ing Participation in Commercial Sharing Systems. J Mark. 2012; 76: 109–125. https://doi.org/10.1509/
                                                 jm.10.0368
                                           24.   Schor JB, Fitzmaurice CJ. Collaborating and connecting: the emergence of the sharing economy.
                                                 Handbook of Research on Sustainable Consumption. Cheltenham, UK; 2015. Available: https://www.
                                                 elgaronline.com/view/9781783471263.00039.xml
                                           25.   Slee T. Some obvious things about internet reputation systems. Retrieved Oct. 2013; 6: 2015.
                                           26.   Strader TJ, Ramaswami SN. The value of seller trustworthiness in C2C online markets. Commun ACM.
                                                 2002; 45: 45–49. https://doi.org/10.1145/585597.585600
                                           27.   Willis J, Todorov A. First impressions: Making up your mind after a 100-ms exposure to a face. Psychol
                                                 Sci. 2006; 17: 592–598. https://doi.org/10.1111/j.1467-9280.2006.01750.x PMID: 16866745
                                           28.   Sofer C, Dotsch R, Wigboldus DHJ, Todorov A. What Is Typical Is Good: The Influence of Face Typical-
                                                 ity on Perceived Trustworthiness. Psychol Sci. 2014; 26: 39–47. https://doi.org/10.1177/
                                                 0956797614554955 PMID: 25512052
                                           29.   Chatterjee P, Gilly MC, Meyers-Levy J. Online Reviews: Do Consumers Use Them? Advances in Con-
                                                 sumer Research Volume. Valdosta, GA: Association for Consumer Research; 2001. pp. 129–133.
                                           30.   Gretzel U, Yoo KH. Use and impact of online travel reviews. In: O’Connor P, Höpken W, Gretzel U, edi-
                                                 tors. Information and communication technologies in tourism. New York: Springer; 2008. pp. 35–46.
                                           31.   Sparks BA, Browning V. The impact of online reviews on hotel booking intentions and perception of
                                                 trust. Tour Manag. 2011; 32: 1310–1323. https://doi.org/10.1016/j.tourman.2010.12.011
                                           32.   Casaló LV, Flavián C, Guinalı́u M. Understanding the intention to follow the advice obtained in an online
                                                 travel community. Comput Hum Behav. 2011; 27: 622–633. https://doi.org/10.1016/j.chb.2010.04.013
                                           33.   Green CH. White Paper: Trust and the Sharing Economy: A New Business Model. Retrieved May.
                                                 2012; 12: 2014.
                                           34.   Yacouel N, Fleischer A. The role of cybermediaries in reputation building and price premiums in the
                                                 online hotel market. J Travel Res. 2012; 51: 219–226. https://doi.org/10.1177/0047287511400611
                                           35.   McKnight DH, Choudhury V, Kacmar C. The impact of initial consumer trust on intentions to transact
                                                 with a web site: a trust building model. J Strateg Inf Syst. 2002; 11: 297–323. https://doi.org/10.1016/
                                                 S0963-8687(02)00020-3
                                           36.   McKnight DH, Choudhury V, Kacmar C. Developing and Validating Trust Measures for e-Commerce:
                                                 An Integrative Typology. Inf Syst Res. 2002; 13: 334–359. https://doi.org/10.1287/isre.13.3.334.81
                                           37.   Ert E, Fleischer A, Magen N. Trust and reputation in the sharing economy: The role of personal photos
                                                 in Airbnb. Tour Manag. 2016; 55: 62–73. https://doi.org/10.1016/j.tourman.2016.01.013
                                           38.   Resnick P, Zeckhauser R. Trust among strangers in internet transactions: Empirical analysis of eBay’ s
                                                 reputation system. Adv Appl Microecon. 2002; 11: 127–157. https://doi.org/10.1016/S0278-0984(02)
                                                 11030-3
                                           39.   Teubner T. Thoughts on the Sharing Economy. Proceedings of the International Conference on e-Com-
                                                 merce. 2014. pp. 322–326.
                                           40.   Park H, Xiang Z, Josiam B, Kim H. Personal profile information as cues of credibility in online travel
                                                 reviews. Anatolia. 2014; 25: 13–23. https://doi.org/10.1080/13032917.2013.820203
                                           41.   Harries C, Evans JSBT, Dennis I. Measuring doctors’ self-insight into their treatment decisions. Appl
                                                 Cogn Psychol. 2000; 14: 455–477. https://doi.org/10.1002/1099-0720(200009)14:5<455::AID-
                                                 ACP667>3.0.CO;2-V
                                           42.   Gigerenzer G, Gaissmaier W. Heuristic Decision Making. Annu Rev Psychol. 2011; 62: 451–482.
                                                 https://doi.org/10.1146/annurev-psych-120709-145346 PMID: 21126183
                                           43.   Harries C, Harvey N. Taking advice, using information and knowing what you are doing. Acta Psychol
                                                 (Amst). 2000; 104: 399–416. https://doi.org/10.1016/S0001-6918(00)00038-X
                                           44.   Harries PA, Harries C. Studying Clinical Reasoning, Part 2: Applying Social Judgement Theory. Br J
                                                 Occup Ther. 2001; 64: 285–292. https://doi.org/10.1177/030802260106400604




PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                            16 / 18
                                                                                                                         Digital Identity and user judgment



                                           45.   Tversky A, Kahneman D. Judgment under uncertainty: Heuristics and biases. In: Kahneman D, Slovic
                                                 P, Tversky A, editors. Judgment under uncertainty. Cambridge University Press; pp. 3–20. https://doi.
                                                 org/10.1017/cbo9780511809477.002
                                           46.   Podsakoff PM, MacKenzie SB, Lee J-Y, Podsakoff NP. Common method biases in behavioral research:
                                                 A critical review of the literature and recommended remedies. J Appl Psychol. 2003; 88: 879–903.
                                                 https://doi.org/10.1037/0021-9010.88.5.879 PMID: 14516251
                                           47.   Livan G, Caccioli F, Aste T. Excess reciprocity distorts reputation in online social networks. Sci Rep.
                                                 2017; 7. https://doi.org/10.1038/s41598-017-03481-7 PMID: 28615619
                                           48.   Tadelis S. The Economics of Reputation and Feedback Systems in E-Commerce Marketplaces. IEEE
                                                 Internet Comput. 2016; 20: 12–19. https://doi.org/10.1109/mic.2015.140
                                           49.   Casler K, Bickel L, Hackett E. Separate but equal? A comparison of participants and data gathered via
                                                 Amazon’s MTurk, social media, and face-to-face behavioral testing. Comput Hum Behav. 2013; 29:
                                                 2156–2160. https://doi.org/10.1016/j.chb.2013.05.009
                                           50.   Slovic P, Lichtenstein S. Comparison of Bayesian and regression approaches to the study of informa-
                                                 tion processing in judgment. Organ Behav Hum Perform. 1971; 6: 649–744. https://doi.org/10.1016/
                                                 0030-5073(71)90033-X
                                           51.   Deane DH, Hammond KR, Summers DA. Acquisition and application of knowledge in complex infer-
                                                 ence tasks. J Exp Psychol. 1972; 92: 20–26. https://doi.org/10.1037/h0032162
                                           52.   Harvey N. Learning judgment and decision making from feedback. Judgm Decis Mak Ski. 2011; 199–
                                                 226. https://doi.org/10.1017/cbo9781139015684.013
                                           53.   Berger CR, Calabrese RJ. Some explorations in initial interaction and beyond: Toward a developmental
                                                 theory of interpersonal communication. Hum Commun Res. 1975; 1: 99–112. https://doi.org/10.1111/j.
                                                 1468-2958.1975.tb00258.x
                                           54.   Salmon SJ, Vet ED, Adriaanse MA, Fennis BM, Veltkamp M, Ridder DTDD. Social proof in the super-
                                                 market: Promoting healthy choices under low self-control conditions. Food Qual Prefer. 2015; 45: 113–
                                                 120. https://doi.org/10.1016/j.foodqual.2015.06.004
                                           55.   Fiske ST, Taylor SE. Social cognition: From brains to culture [Internet]. London, UK: SAGE Publica-
                                                 tions Limited; 2013. Available: http://dx.doi.org/10.4135/9781446286395
                                           56.   Ariely D, Loewenstein G, Prelec D. “Coherent Arbitrariness”: Stable Demand Curves Without Stable
                                                 Preferences. Constr Prefer. 2003; 118: 246–270. https://doi.org/10.1017/cbo9780511618031.014
                                           57.   Nisbett RE, Wilson TD. Telling more than we can know: Verbal reports on mental processes. Psychol
                                                 Rev. 1977; 84: 231–259. https://doi.org/10.1037/0033-295x.84.3.231
                                           58.   Estes WK. The cognitive side of probability learning. Psychol Rev. 1976; 83: 37–64. https://doi.org/10.
                                                 1037/0033-295x.83.1.37
                                           59.   Pouget A, Drugowitsch J, Kepecs A. Confidence and certainty: distinct probabilistic quantities for differ-
                                                 ent goals. Nat Neurosci. 2016; 19: 366–374. https://doi.org/10.1038/nn.4240 PMID: 26906503
                                           60.   Camerer CF, Hogarth RM. J Risk Uncertain. 1999; 19: 7–42. https://doi.org/10.1023/a:1007850605129
                                           61.   Holt CA, Laury SK. Risk Aversion and Incentive Effects. Am Econ Rev. 2002; 92: 1644–1655. https://
                                                 doi.org/10.1257/000282802762024700
                                           62.   Kahneman D, Peavler WS. Incentive effects and pupillary changes in association learning. J Exp Psy-
                                                 chol. 1969; 79: 312–318. https://doi.org/10.1037/h0026912 PMID: 5785645
                                           63.   Acquisti A, Taylor C, Wagman L. The Economics of Privacy. J Econ Lit. 2016; 54: 442–92. https://doi.
                                                 org/10.1257/jel.54.2.442
                                           64.   Bansal HS, Voyer PA. World-of-mouth processes within a services purchase decision context. J Serv
                                                 Res. 2000; 3: 166–177. https://doi.org/10.1177/109467050032005
                                           65.   Garcia-Retamero R, Rieskamp J. Do people treat missing information adaptively when making infer-
                                                 ences? Q J Exp Psychol. 2009; 62: 1991–2013. https://doi.org/10.1080/17470210802602615 PMID:
                                                 19241222
                                           66.   Jøsang A, Ismail R, Boyd C. A survey of trust and reputation systems for online service provision. Decis
                                                 Support Syst. 2007; 43: 618–644. https://doi.org/10.1016/j.dss.2005.05.019
                                           67.   Resnick P, Kuwabara K, Zeckhauser R, Friedman E. Reputation Systems. Commun ACM. 2000; 43:
                                                 45–48. https://doi.org/10.1145/355112.355122
                                           68.   Emerson RM. Social Exchange Theory. Annu Rev Sociol. 1976; 2: 335–362. https://doi.org/10.1146/
                                                 annurev.so.02.080176.002003
                                           69.   Shah JY, Gardner WL. Handbook of motivation science. Guilford Press; 2008.
                                           70.   Tedjamulia SJJ, Dean DL, Olsen DR, Albrecht CC. Motivating Content Contributions to Online Commu-
                                                 nities: Toward a More Comprehensive Theory. Proceedings of the 38th Annual Hawaii International
                                                 Conference on System Sciences. IEEE; doi:10.1109/hicss.2005.444




PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                            17 / 18
                                                                                                                         Digital Identity and user judgment



                                           71.   Bambauer-Sachse S, Mangold S. Brand equity dilution through negative online word-of-mouth commu-
                                                 nication. J Retail Consum Serv. 2011; 18: 38–45. https://doi.org/10.1016/j.jretconser.2010.09.003
                                           72.   van der Werff L, Real C, Lynn T. Individual trust and the internet. In: Searle R, Nienaber A, Sitkin SB,
                                                 editors. Trust. Oxford, Untied Kingdom: Routledge; 2018.




PLOS ONE | https://doi.org/10.1371/journal.pone.0209071 December 13, 2018                                                                            18 / 18
