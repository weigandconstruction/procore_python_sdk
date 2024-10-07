# ChecklistDefaultResponseSet1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conforming_response** | **str** | Term used to represent conforming statuses on items within the current template, e.g. \&quot;Pass\&quot; or \&quot;Safe\&quot;. This maps to an item status of \&quot;yes\&quot;. | [optional] 
**deficient_response** | **str** | Term used to represent deficient statuses on items within the current template, e.g. \&quot;Fail\&quot; or \&quot;At Risk\&quot;.  This maps to an item status of \&quot;no\&quot;. | [optional] 
**var_global** | **bool** | Represents whether a response set has been provided by Procore. | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 

## Example

```python
from procore_sdk.models.checklist_default_response_set1 import ChecklistDefaultResponseSet1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistDefaultResponseSet1 from a JSON string
checklist_default_response_set1_instance = ChecklistDefaultResponseSet1.from_json(json)
# print the JSON string representation of the object
print(ChecklistDefaultResponseSet1.to_json())

# convert the object into a dict
checklist_default_response_set1_dict = checklist_default_response_set1_instance.to_dict()
# create an instance of ChecklistDefaultResponseSet1 from a dict
checklist_default_response_set1_from_dict = ChecklistDefaultResponseSet1.from_dict(checklist_default_response_set1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


