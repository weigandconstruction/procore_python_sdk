# ProjectPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The First Name of the Project Person | [optional] 
**last_name** | **str** | The Last Name of the Project Person | 
**is_employee** | **bool** | The Employee status of the Project Person | [optional] [default to False]
**employee_id** | **str** | The Employee ID of the Project Person | [optional] 
**origin_id** | **str** | The ID of the External Data associated with the Project Person | [optional] 

## Example

```python
from procore_sdk.models.project_person import ProjectPerson

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPerson from a JSON string
project_person_instance = ProjectPerson.from_json(json)
# print the JSON string representation of the object
print(ProjectPerson.to_json())

# convert the object into a dict
project_person_dict = project_person_instance.to_dict()
# create an instance of ProjectPerson from a dict
project_person_from_dict = ProjectPerson.from_dict(project_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


