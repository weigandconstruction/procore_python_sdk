# ProjectBidType2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Bid Type ID | [optional] 
**name** | **str** | Project Bid Type name | [optional] 

## Example

```python
from procore_sdk.models.project_bid_type2 import ProjectBidType2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBidType2 from a JSON string
project_bid_type2_instance = ProjectBidType2.from_json(json)
# print the JSON string representation of the object
print(ProjectBidType2.to_json())

# convert the object into a dict
project_bid_type2_dict = project_bid_type2_instance.to_dict()
# create an instance of ProjectBidType2 from a dict
project_bid_type2_from_dict = ProjectBidType2.from_dict(project_bid_type2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


