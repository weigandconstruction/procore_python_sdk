# ExtendedView2BiddingDistributionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Email | [optional] 
**company_name** | **str** | name of company | [optional] 
**id** | **int** | Login Information ID of the User | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.extended_view2_bidding_distribution_inner import ExtendedView2BiddingDistributionInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedView2BiddingDistributionInner from a JSON string
extended_view2_bidding_distribution_inner_instance = ExtendedView2BiddingDistributionInner.from_json(json)
# print the JSON string representation of the object
print(ExtendedView2BiddingDistributionInner.to_json())

# convert the object into a dict
extended_view2_bidding_distribution_inner_dict = extended_view2_bidding_distribution_inner_instance.to_dict()
# create an instance of ExtendedView2BiddingDistributionInner from a dict
extended_view2_bidding_distribution_inner_from_dict = ExtendedView2BiddingDistributionInner.from_dict(extended_view2_bidding_distribution_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


