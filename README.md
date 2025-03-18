# For Details Refernce Following Articles
1. https://medium.com/@idrees535/an-analytical-framework-to-design-liquidity-mining-incentives-program-7aab444e3f88
2. https://medium.com/@idrees535/expanding-gauntlets-liquidity-mining-analysis-towards-an-optimized-framework-for-liquidity-mining-267681da029d
3. https://medium.com/gauntlet-networks/uniswap-liquidity-mining-analysis-14c739c54a9d
4. https://gov.uniswap.org/t/uniswap-incentive-design-analysis/21662
   
# V1: Designing-Effective-Liquidity-Mining-Programs-A-Data-Driven-Approach
This repository contains Python code and Jupyter notebooks which perform a detailed analysis of liquidity Mining incentives. The analysis is inspired by Gauntlet Network's study and is extended to explore different facets of liquidity mining.  The goal of the analysis is to provide insights for designing effective liquidity mining programs.
Expanding Gauntlet's Liquidity Mining Analysis: Towards an Optimized Framework for Liquidity Mining Program Design
# Background
In 2022 and 2023, Uniswap implemented an experiment with the aim of distributing UNI incentives to liquidity providers (LPs) of specific Uniswap pools on Optimism. On June 7, 2023, a report by Gauntlet suggested that categorizing Uniswap's Liquidity Mining (LM) program as a failure in stimulating sustainable Total Value Locked (TVL) growth and trading volume may not be entirely accurate. While it is true that the growth in TVL and volume attained by the incentivized pools diminished following the cessation of rewards, the new equilibrium reached by these pools was substantially higher than the level prior to the introduction of incentives. This observation supports the assertion that if properly structured and sufficiently incentivizing for LPs, LM programs can indeed serve as a tool for bootstrapping new liquidity providers. Furthermore, it was suggested that the impacts of LM programs on the TVL and volume of a pool extend beyond the period of the LM program itself.
# Introduction
In the realm of Decentralized Finance (DeFi), providing a seamless and profitable experience for liquidity providers is a crucial determinant of a protocol's success. An effective way to attract and incentivize liquidity providers is through Liquidity Mining Programs. These programs reward providers with additional tokens, enhancing their return on investment and promoting longer-term commitment to the protocol.
The design of an effective Liquidity Mining Program requires careful consideration and analysis of past data. By understanding how previous incentives have influenced the behavior of liquidity providers, protocols can design more effective future programs. This article seeks to analyze the data from Uniswap's recent incentive program, drawing insights that may guide the design of future Liquidity Mining Programs.
The Importance of Designing Effective Liquidity Mining Programs
The primary goal of a Liquidity Mining Program is to attract more liquidity to the protocol. By incentivizing providers with additional tokens, the protocol can attract a larger pool of liquidity, leading to improved price stability, less slippage, and a better overall experience for traders. However, designing such a program is not without its challenges.
Incentives must be carefully calibrated to ensure they are attractive enough to draw in liquidity providers without unduly diluting the token supply. The selection of which pools to incentivize is also crucial, as it can influence the protocol's asset composition and impact its risk profile. To make these decisions effectively, it's essential to analyze data from past programs and understand how they've impacted provider behavior and protocol health.
# Part 1: Replicating Gauntlet's Analysis

Our exploration begins by replicating the seminal analysis conducted by Gauntlet Networks. Gauntlet's research was centered around a comparison between two types of Uniswap pools:
Treatment pools - Pools that were recipients of additional incentives via the liquidity mining program.
Control pools - Pools that did not receive any extra incentives.
Gauntlet's findings suggested that incentivized pools witnessed substantial growth in total value locked (TVL) and fees during the incentive period.
Our replication of this study, using data directly from the Uniswap Subgraph, yielded similar results. This established a strong foundation to further delve into the intricacies of the data.
For details of this analysis refer to Gauntlet's article
Market Share in different Intervals 
TVL Market Share:
Lift during: 25.03% (p < 0.01)
Lift after: -23.90% (p = 1.00)
Fee Market Share:
Lift during: 28.10% (p < 0.01)
Lift after: -7.32% (p = 0.45)
(There is some difference in obtained resultsin comparison with Gauntlet's analysis due difference in intervals of before and after periods and price normalization which isn't implemented in this analysis)
Treatment vs Control tvlUSDTreatment vs Control tvlUSDTVL Market share comparisonFee Market share Comparison

# Part 2: Exploring the Treatment Pools
Beyond replicating Gauntlet's analysis, we took a step further to explore the data of the treatment pools. Our goal was to gain insights that could be beneficial in designing an effective liquidity mining program.

## Metrics Variability
Here are the plots showing how Total Value Locked (TVL), Volume, and Fees have changed over time for each of the four pools (wstETH-WETH, WETH-DAI, USDC-DAI, OP-USDC).
As you can see, each pool has different dynamics. Some pools, like wstETH-WETH, have seen significant increases in TVL, Volume, and Fees during the period of the liquidity mining program. Others, like OP-USDC, have seen more modest increases.
Based on these observations, here are some potential insights for designing a liquidity mining program:
Choosing Pools: Pools with higher initial TVL, Volume, and Fees may respond more positively to liquidity mining programs. In your case, you might want to target pools with similar characteristics.
Incentive Amount: The amount of incentives might need to be adjusted based on the characteristics of the pool. Pools with higher initial TVL may require larger incentives to motivate liquidity providers.
Duration: The impact of the liquidity mining program seems to last even after the program has ended, although it does decrease over time. Therefore, the duration of the program might need to be balanced against the desired long-term impact.

## Coorelation
The correlation matrix provides a measure of how closely related the 'tvlUSD', 'volumeUSD', and 'feesUSD' variables are. A value close to 1 indicates a strong positive correlation, a value close to -1 indicates a strong negative correlation, and a value close to 0 indicates no correlation.
From the correlation matrix, we can observe:
'tvlUSD' (Total Value Locked in USD) has a positive correlation with 'volumeUSD' and 'feesUSD'. This indicates that as the total value locked in the pool increases, the trading volume and fees generated by the pool also tend to increase.
'volumeUSD' and 'feesUSD' have a strong positive correlation. This indicates that as the trading volume in the pool increases, the fees generated by the pool also tend to increase.

These correlations suggest that incentivizing pools with higher TVL could lead to higher trading volumes and more fees generated, which could make the liquidity mining program more effective.

## Pools Comparison
For a comparative analysis of the four pools we can calculate the average 'tvlUSD', 'volumeUSD', and 'feesUSD' for each pool during the LM program period. This can give us an idea of which pools performed the best during the LM program.
The table below shows the average Total Value Locked (TVL), trading volume, and fees generated for each of the four pools during the liquidity mining (LM) program period.
From this table, we can make a few observations:
The USDC-DAI pool had the highest average TVL during the LM program, followed by WETH-DAI, OP-USDC, and wstETH-WETH.
The OP-USDC pool had the highest trading volume during the LM program, followed by USDC-DAI, WETH-DAI, and wstETH-WETH.
The OP-USDC pool also generated the most fees during the LM program, followed by WETH-DAI, USDC-DAI, and wstETH-WETH.
These insights suggest that different pools might respond differently to liquidity mining programs, and the choice of pools to include in the program could have a significant impact on the program's success. For your LM program, you might want to consider including a mix of pools that have demonstrated high TVL, volume, and fee generation in past LM programs.
Also, it's worth noting that these are just average values, and the actual performance of each pool can vary from day to day. For a more nuanced understanding of each pool's performance, you could look at the distribution of these metrics over time or perform a more detailed time series analysis.

## Time Series Decomposition
The following plots represent the time series decomposition of 'tvlUSD' and 'volumeUSD' for each of the four pools. This decomposition breaks down the time series into three components:
Trend: The increasing or decreasing value in the series.
Seasonality: The repeating short-term cycle in the series.
Residuals: The random variation in the series.
Here are some observations from these plots:
For all four pools, the trend in 'tvlUSD', 'volumeUSD', and 'feesUSD' appears to be increasing during the liquidity mining (LM) program.
The seasonality component is quite apparent for 'volumeUSD' and 'feesUSD', suggesting there may be specific days of the week when volume and fees are higher. This could be due to various factors such as trading patterns of liquidity providers or market movements.
The residuals, representing the random variation not explained by the trend or seasonality, seem to be fairly consistent over time. Any large spikes in residuals could be due to external factors not captured in our data.
These observations provide more detailed insights into the behavior of each pool during the LM program. Understanding these dynamics can help inform the design of your own LM program. For example, recognizing a strong weekly seasonality pattern could influence the timing of your LM program or the frequency of reward distribution.
# Future Work
The analysis presented here serves as a stepping stone towards a deeper understanding of Liquidity Mining Programs. However, there is much more to explore in this field, and the following are some avenues for future work:
1. Multiple Treatment Groups: Analyzing the impact of different levels or types of incentives on multiple treatment groups could provide insights into how varying incentive structures influence pool behavior.
2. Long-Term Impact Analysis: Extending the timeframe of the analysis could shed light on the long-term impacts of incentives. Do pools eventually return to their pre-incentive behavior, or do they maintain some of the gains even long after incentives have ended?
3. Individual Behavior Analysis: Understanding individual behavior within the pools could reveal patterns or common characteristics among participants who contribute disproportionately to the increase in TVL or fees.
4. Correlation with External Factors: Examining how external factors, such as overall market conditions or specific events, impact the effectiveness of incentives could provide valuable context for interpreting the results of an incentive program.
5. Alternative Metrics: Considering other metrics like the number of active participants in a pool, the number of transactions, or the average transaction size could provide a more comprehensive picture of a pool's performance and response to incentives.
6. Prediction Modeling: Based on the data, creating a model to predict the impact of future incentive programs could be a valuable tool for protocols planning their next Liquidity Mining Program.
By further exploring these areas, we can continue to refine and optimize Liquidity Mining Programs, maximizing their effectiveness and benefit to both liquidity providers and the wider DeFi ecosystem.

# V2: Framework to design LM Incentive Program
The Analytical Framework
Thesis statement

By inheriting the assumptions of trader and LP elasticity we establish that following indicator is efficient matric of a pool performance. Therefore we can use pool efficiency matrix first to filter pools which we want to incentivize through liquidity mining incentive program. and then we can use this b matrix to estimate the amount of incentives which we want to allocate for each pool.

## Matrices

Our framework for designing liquidity mining incentives is based on the concept of Return on Investment (ROI), defined as:

ROI = (Current Value of Investment−Cost of Investment / Cost of Investment) × 100%

Where:

- Current Value of Investment = TVL (USD) + Fee (USD) + Incentives — Impermanent Loss (IL)

- Cost of Investment = TVL (USD)

For simplicity, we do not incorporate IL in this iteration of the performance matrix. We propose the following matrix as an efficient measure of a pool’s performance:

ROI = Fee (USD) / TVL (USD)

## Assumptions
LPs and traders are elastic to their returns and execution price respectively

feesUSD/tvlUSD is correct indicatorto measure the performance of Pools

## Limitations
Following are limitations of this model which will addressed in future versions of this Framework

1. As data of comparative pools is not incorporated in this iteration of framework, so defining baseline ROIand target tvl based on data of uniswap pools is not most efficient approach, hence incorporating data of other dexes will produce much better results

2. TVL growth model was trained on data of optimism uniswap v3 pools, due to very limited dataset the accuracy of tvl growth model will be compromised, by incorporating more data in tvl growth model

3. TVL growth model is not tuned due to absence of validation/dev set, incorporating more data will enable to define a better architecture of LSTM model and tune it’s parameters

## Filtering Pools

We first filter out the pools that are already performing well, as the margin for improvement through incentives is minimal for these pools.

Baseline Performance Analysis

For underperforming pools, we establish a baseline ROI which is used to filter pools, define targeted tvl of pools and for incentive allocation

baseline_roi = avg_monthly_roi

In first iteration of framework design, we are using average monthly roi of top 20 pools as baseline roi standard


## Defining Target ROI

The target ROI should be set higher than the baseline ROI to incentivize LPs. The difference between the target and current ROI is the amount of incentives required to achieve the target ROI.

Targeted_ROI = Baseline_ROI + surplus

## Calculating Incentive Allocation

Based on the previous TVL data, we forecast the TVL for the next period (LM incentive period) and calculate the incentive allocation for each pool required to achieve the desired ROI.

Incentive_allocation = differnce_ROI * estimated_tvl

## Evaluating the Effectiveness of LM Incentives
We propose two models to evaluate the effectiveness of the LM incentives:

1. Target TVL Model: If the TVL of the pool reaches the targeted level, considering the elasticity of traders, the volume will increase, resulting in more fees for LPs. This will allow LPs to achieve surplus ROI during the incentive period and retain their positions even when the incentives are discontinued.

2. TVL Growth Model: This model uses historical data of TVL growth and incentive spend amount to simulate the growth of the TVL during the incentive period.

## TVL Growth Model
If the potential TVL growth is greater than the targeted TVL, the LM program is considered a success. Otherwise, it is considered a failure.

# Future Work
Future work is intended to verify the assumptions of this framework and address the limitations of the this Framework by incorporating more data

Incorporate more Data
1. Incorporate data of competitive pools on other dexes (Curve, Balancer, Sushiswap) to define baseline roi based on comparative data

2. Incorporate more data from liquidity mining programs to train growth model

## Improve TVL Growth Model
Use a pool-agnostic feature: Instead of using absolute TVL values, use tvl market share feature that is pool-agnostic (Incorporate data of competitive pools).

Feature Engineering: Consider additional features to add that could help the model distinguish between different pools (incentives/tvlUSD, ROI/incentives, adv/Incentives)

As a ratio: Consider incorporating the incentive amount as a ratio with the TVL (Total Value Locked) value. This might make more sense as it gives a relative measure of how large the incentive is compared to the total value locked.

Using it to modify the output: Another approach could be to use the incentive amount to modify the output of the model. For example, train model to predict the change in TVL, and then use (incentives/avg_tvlUSD)*predicted_tvl to modify output

Hybrid Model: A different approach could be to use a hybrid model. In this case, you could use your LSTM model to predict the TVL based on the time series data, and another machine learning model (like a linear regression) to predict the impact of the incentives on the TVL. The final prediction would then be a combination of these two predictions.

Optimize Incentives Allocation by using feedback loop (cadCAD simulations)
1. Instead of using adv or feesUSD/tvlUSD as performnace matrix, define a more comrehensive performance matrix by incorporating uniswap’s objective function

2. Incorporate feedback of tvl growth model to optimize incentives

# Conclusion
Designing an effective liquidity mining program is a complex task that requires a deep understanding of market dynamics and participant behavior. This proposed analytical framework provides a systematic approach to this task, offering a robust tool for protocol developers and DeFi enthusiasts. Looking forward to refining this framework for efficient Incentive Design
