# CorrespondenceFrom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** | Recipients first name | [optional] 
**last** | **str** | Recipients last name | [optional] 

## Example

```python
from procore_sdk.models.correspondence_from import CorrespondenceFrom

# TODO update the JSON string below
json = "{}"
# create an instance of CorrespondenceFrom from a JSON string
correspondence_from_instance = CorrespondenceFrom.from_json(json)
# print the JSON string representation of the object
print(CorrespondenceFrom.to_json())

# convert the object into a dict
correspondence_from_dict = correspondence_from_instance.to_dict()
# create an instance of CorrespondenceFrom from a dict
correspondence_from_from_dict = CorrespondenceFrom.from_dict(correspondence_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


