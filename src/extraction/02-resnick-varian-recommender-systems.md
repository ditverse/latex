# Recommender Systems

Sumber PDF: $(System.Collections.Hashtable.file)

---

Recom
                Paul Resnick and Hal R. Varian, Guest Editors


Recommender
   Systems
 I SystT IS OFTEN NECESSARY TO MAKE CHOICES WITHOUT SUFFICIENT
    personal experience of the alternatives. In everyday life, we rely on
    recommendations from other people either by word of mouth, rec-
ommendation letters, movie and book reviews printed in newspapers, or
general surveys such as Zagatâ€™s restaurant guides.
   Recommender systems assist and augment this
natural social process. In a typical recommender sys-
tem people provide recommendations as inputs,
which the system then aggregates and directs to
appropriate recipients. In some cases the primary
transformation is in the aggregation; in others the
systemâ€™s value lies in its ability to make good matches
                                                             URLs; and Siteseer mines personal bookmark lists.
                                                             Third, recommendations may be anonymous, tagged
                                                             with the sourceâ€™s identity, or tagged with a pseudo-
                                                             nym. The fourth dimension, and one of the richest
                                                             areas for exploration, is how to aggregate evaluations.
                                                             GroupLens, PHOAKS, and Siteseer employ variants
                                                             on weighted voting. Fab takes that one step further to
between the recommenders and those seeking recom-            combine evaluations with content analysis. Referral-
mendations.                                                  Web combines suggested links between people to form
   The developers of the first recommender system,           longer referral chains. Finally, the (perhaps aggregated)
Tapestry [1], coined the phrase â€œcollaborative filteringâ€    evaluations may be used in several ways: negative rec-
and several others have adopted it. We prefer the more       ommendations may be filtered out, the items may be
general term â€œrecommender systemâ€ for two rea-                       sorted according to numeric evaluations, or
sons. First, recommenders may not explictly                              evaluations may accompany items in a dis-
collaborate with recipients, who may be                                    play.
unknown to each other. Second, recom-                                            Figures 2 and 3 identify dimensions
mendations may suggest particularly                                           of the domain space: The kinds of
interesting items, in addition to indicat-                                    items being recommended and the
ing those that should be filtered out.                                        people among whom evaluations are
   This special section includes descrip-                                    shared. Consider, first, the domain of
tions of five recommender systems. A sixth                                 items. The sheer volume is an important
article analyzes incentives for provision of rec-                        variable: Detailed textual reviews of restau-
ommendations.                                                        rants or movies may be practical, but applying
   Figure 1 places the systems in a technical design         the same approach to thousands of daily Netnews mes-
space defined by five dimensions. First, the contents of     sages would not. Ephemeral media such as netnews
an evaluation can be anything from a single bit (rec-        (most news servers throw away articles after one or two
ommended or not) to unstructured textual annota-             weeks) place a premium on gathering and distributing
tions. Second, recommendations may be entered                evaluations quickly, while evaluations for 19th century
explicitly, but several systems gather implicit evalua-      books can be gathered at a more leisurely pace. The
tions: GroupLens monitors usersâ€™ reading times;              last dimension describes the cost structure of choices
PHOAKS mines Usenet articles for mentions of                 people make about the items. Is it very costly to miss

56     March 1997/Vol. 40, No. 3 COMMUNICATIONS OF THE ACM
mmende
                                                                                                                      ecommender Systems
 a good item or sample a bad one? How do those costs            uisite for receiving recommendations or by offering
 compare to the benefits of hitting a good one? This            monetary compensation. Second, if anyone can provide
 cost structure is likely to interact with technical design     recommendations, content owners may generate
 choices. For example, when the costs of incorrect deci-        mountains of positive recommendations for their own
 sions are high, as they would be, say, with evaluations        materials and negative recommendations for their
 of medical treatments, evaluations that convey more            competitors. Future systems are likely to introduce
 nuances are likely to be more useful.                          precautions that discourage the â€œvote early and oftenâ€
    Next, consider the set of recommendations and the           phenomenon.
 people providing and consuming them. Who provides                 Recommender systems also raise concerns about




                                                                                                                                     Future systems will likely need to offer some incentive for providing recommendations.
 recommendations? Do they tend to evaluate many                 personal privacy. In general, the more information




 tems
 items in common, leading to a dense set of recommen-           individuals have about the recommendations, the bet-
 dations? How many consumers are there, and do their            ter they will be able to evaluate those recommenda-
 tastes vary? These factors also will interact with techni-     tions. However, people may not want their habits or
 cal choices. For example, matching people by tastes            views widely known. Some recommender systems per-
 automatically is far more valuable in a larger set of peo-     mit anonymous participation or participation under a
 ple who may not know each other. Personalized aggre-           pseudonym, but this is not a complete solution since
 gation of recommendations will be more valuable when           some people may desire an intermediate blend of pri-
 peopleâ€™s tastes differ than when there are a few experts.      vacy and attributed credit for their efforts.
                                                                   Both incentive and privacy problems arise in an
 Social Implications                                            evaluation-sharing system familiar to our readers: the
 Recommender systems introduce two interesting                  peer review system used in academia. With respect to
 incentive problems. First, once one has established a          incentives, every editor knows the best source for a
 profile of interests, it is easy to free ride by consuming     prompt and careful review is an author who currently
 evaluations provided by others. Moreover, as Avery and         has an article under consideration. With respect to pri-
 Zeckhauser argue, this problem is not entirely solved          vacy, blind and double-blind refereeing are common
 even if evaluations are gathered implicitly from exist-        practices. These practices evolved to solve problems
 ing resources or from monitoring user behavior. Future         inherent to the refereeing process, and it may be worth-
 systems will likely need to offer some incentive for the       while to consider ways to incorporate such practices
 provision of recommendations by making it a prereq-            into automated systems.
 Figure 1.
 The                            Contents of        Explicit                                                    Use of
                             recommendation        entry?        Anonymous?          Aggregation          recommendations
 technical
 design      GroupLens         a) numeric: 1â€“5    a) explicit    pseudonymous       personalized            display alongside
 space                                                                              weighting based         articles in
                               b) seconds         b) monitor                        on past                 existing summary
                                                  reading                           agreement               views
                                                  time                              among
                                                                                    recommenders

             Fab               numeric: 1â€“7       explicit       pseudonymous       personalized            selection/
                                                                                    weighting;              filtering
                                                                                    combined with
                                                                                    content analysis

             ReferralWeb       mention of a       mined          attributed         assemble referral       display
                               person or a        from                              chain to desired
                               document           public data                       person
                                                  sources

             PHOAKS            mention of a       mined          attributed         one person one          sorted display
                               URL                from                              vote (per URL)
                                                  usenet
                                                  postings

             Siteseer          mention of a       mined          anonymous          frequency of            display
                               URL                from                              mention in
                                                  existing                          overlapping
                                                  bookmark                          folders
                                                  folders



                                                                        COMMUNICATIONS OF THE ACM March 1997/Vol. 40, No. 3     57
                       Type of items          How many        Lifetime          Cost structure            between unbiased rec-
                                                                                                          ommendations and
  GroupLens          netnews           thousands          1â€“2           misses unimportant                advertisements in order
                     articles          per day            weeks         false positive very small         to maintain credibility
                                                                        cost hits small value
                                                                                                          with their readers.
  PHOAKS,            URLs              hundreds           2 daysâ€“       misses unimportant                    There are economies
  SiteSeer, Fab                        per day            2 yesars      false positives small cost of scale in recommender
                                                                        hits medium value
                                                                                                          systems: The bigger the
  ReferralWeb        people            a few million      many          depends on how referral set of users, the more
                                       reachable          years         chain will be used                likely I am to find
                                       on-line
                                                                                                          someone like me.
Figure 2. The domain spaceâ€”characteristics of items evaluated                                             Hence, other things
                                              Density of                                 Comsumer being equal, I would
                   Recommenders         recommendations            Consumers                 Taste        prefer to use the biggest
                                                                                          variability system. When several
 GroupLens          All subscribers    somewhat dense within         Subscribers         high for some recommender systems
                                       newsgroup                                         newsgroups start to compete in a

 Fab                All subscribers    somewhat dense among          Subscribers         unknown
                                                                                                          given market, we
                                       people served by same                                              should expect to see
                                       collector agent                                                    very intense competi-
 ReferralWeb        All authors of     reflects density of           Any Web             unknown
                                                                                                          tion since there is likely
                    on-line            underlying social             user                                 to be only one eventual
                    documents          network                                                            survivor. This argument
 PHOAKS             All usenet         extremely sparse              Any Web             unknown          suggests that a possible
                    authors                                          user                                 market structure will be
                                                                                                          one or two big players
 Siteseer           All subscribers    sparse                        Subscribers         high
                                                                                                          in each medium or sub-
Figure 3. The domain spaceâ€”characteristics of the participants and the set of evaluations                 ject area who then sub-
                                                                                                          contract with sellers of
Business Models                                                 products to provide recommendations as a value-added
Maintenance of a recommender system is costly, and it service. For example, a book rating/review service might
is worth thinking about what business models might operate autonomously and sell its recommendation ser-
be used to generate revenues sufficient to cover those vices to a number of independent online bookstores. It
costs. One model is to charge recipients of recommen- should be noted the independence of the rating/review
dations either through subscriptions or pay-per-use. A service may also help to solve the problem of credibility.
second model for cost recovery is advertiser support, as           A flurry of commercial ventures have recently intro-
Firefly (http://www.firefly.com) seems to provide. Pre- duced recommender systems for products ranging from
sumably advertisers would find such systems very use- Web URLs to music, videos, and books. In the coming
ful since they generate detailed marketing information years, we can look forward to continued technical inno-
about consumers. If a user revealed a taste for, say, vation, and a better understanding of which technical
cyberpunk books, publishers could make sure the users features are best suited to various characteristics of the
saw ads targeted to that market. A third model is to items evaluated and the people who participate in the
charge a fee to the owners of the items being evaluated. process. c
For example, filmmakers pay a fee for official ratings of
their movies.                                                   Reference
   The latter two business models both carry a danger 1. Goldberg,             D. Nichols, D., Oki, B. M., and Terry, D. Using collabora-
                                                                   tive filtering to weave an information tapestry. Commun. ACM 35, 12
of corruption. Mass market computer magazines that                 (Dec.1992), 61â€”70.
carry ads and reviews are often accused of biasing
reviews toward companies that are heavy advertisers. In Paul Resnick (presnick@research.att.com) works for AT&T
this case, the perception of bias is almost as bad as the Labs-Research         in Murray Hill, N.J.
                                                                Hal R. Varian (hal@sims.berkeley.edu) is Dean of the School
reality. Recommender systems that collect fees from of Information Management and Systems at the University of
advertisers or others who may have a vested interest in California, Berkeley.
the contents of the recommendations must be very
careful to make sure that users recognize the difference Â© ACM 0002-0782/97/0300 $3.50

58      March 1997/Vol. 40, No. 3 COMMUNICATIONS OF THE ACM

