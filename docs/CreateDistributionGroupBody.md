# CreateDistributionGroupBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distribution_group** | [**DistributionGroup**](DistributionGroup.md) |  | 

## Example

```python
from procore_sdk.models.create_distribution_group_body import CreateDistributionGroupBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDistributionGroupBody from a JSON string
create_distribution_group_body_instance = CreateDistributionGroupBody.from_json(json)
# print the JSON string representation of the object
print(CreateDistributionGroupBody.to_json())

# convert the object into a dict
create_distribution_group_body_dict = create_distribution_group_body_instance.to_dict()
# create an instance of CreateDistributionGroupBody from a dict
create_distribution_group_body_from_dict = CreateDistributionGroupBody.from_dict(create_distribution_group_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


