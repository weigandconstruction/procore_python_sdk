# DistributionGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Distribution Group | 
**description** | **str** | Description | [optional] 
**user_ids** | **List[int]** | User IDs to associate with the Distribution Group | [optional] 

## Example

```python
from procore_sdk.models.distribution_group import DistributionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionGroup from a JSON string
distribution_group_instance = DistributionGroup.from_json(json)
# print the JSON string representation of the object
print(DistributionGroup.to_json())

# convert the object into a dict
distribution_group_dict = distribution_group_instance.to_dict()
# create an instance of DistributionGroup from a dict
distribution_group_from_dict = DistributionGroup.from_dict(distribution_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


