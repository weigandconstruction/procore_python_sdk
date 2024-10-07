# DistributionGroup1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Distribution Group | [optional] 
**description** | **str** | Description | [optional] 
**user_ids** | **List[int]** | User IDs to associate with the Distribution Group | [optional] 

## Example

```python
from procore_sdk.models.distribution_group1 import DistributionGroup1

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionGroup1 from a JSON string
distribution_group1_instance = DistributionGroup1.from_json(json)
# print the JSON string representation of the object
print(DistributionGroup1.to_json())

# convert the object into a dict
distribution_group1_dict = distribution_group1_instance.to_dict()
# create an instance of DistributionGroup1 from a dict
distribution_group1_from_dict = DistributionGroup1.from_dict(distribution_group1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


