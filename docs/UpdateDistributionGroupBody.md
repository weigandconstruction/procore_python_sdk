# UpdateDistributionGroupBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distribution_group** | [**DistributionGroup1**](DistributionGroup1.md) |  | 

## Example

```python
from procore_sdk.models.update_distribution_group_body import UpdateDistributionGroupBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDistributionGroupBody from a JSON string
update_distribution_group_body_instance = UpdateDistributionGroupBody.from_json(json)
# print the JSON string representation of the object
print(UpdateDistributionGroupBody.to_json())

# convert the object into a dict
update_distribution_group_body_dict = update_distribution_group_body_instance.to_dict()
# create an instance of UpdateDistributionGroupBody from a dict
update_distribution_group_body_from_dict = UpdateDistributionGroupBody.from_dict(update_distribution_group_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


