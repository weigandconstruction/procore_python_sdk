# ProjectBidType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Bid Type ID | [optional] 
**name** | **str** | Project Bid Type name | [optional] 

## Example

```python
from procore_sdk.models.project_bid_type import ProjectBidType

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBidType from a JSON string
project_bid_type_instance = ProjectBidType.from_json(json)
# print the JSON string representation of the object
print(ProjectBidType.to_json())

# convert the object into a dict
project_bid_type_dict = project_bid_type_instance.to_dict()
# create an instance of ProjectBidType from a dict
project_bid_type_from_dict = ProjectBidType.from_dict(project_bid_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


