# BidProject

Project Info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**address** | **str** | Address | [optional] 

## Example

```python
from procore_sdk.models.bid_project import BidProject

# TODO update the JSON string below
json = "{}"
# create an instance of BidProject from a JSON string
bid_project_instance = BidProject.from_json(json)
# print the JSON string representation of the object
print(BidProject.to_json())

# convert the object into a dict
bid_project_dict = bid_project_instance.to_dict()
# create an instance of BidProject from a dict
bid_project_from_dict = BidProject.from_dict(bid_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


