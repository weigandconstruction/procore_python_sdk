# SpecificationSectionRevision

A version of a Specification Section. Each time a Specification Section is revised, the newly uploaded version is a new revision of that section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**specification_section_id** | **int** |  | [optional] 
**specification_section_division_id** | **int** | Id of the Section Division | [optional] 
**specification_set_id** | **int** | Id of the Set | [optional] 
**number** | **str** | The number of this revision&#39;s SpecificationSection | [optional] 
**description** | **str** | The description of this revision&#39;s SpecificationSection | [optional] 
**url** | **str** | Address of SpecificationRevision PDF. This can be blank if the Specification Section was created manually without an upload, and no revisions have been uploaded yet. | [optional] 
**revision** | **str** | The revision number | [optional] 
**issued_date** | **date** | The date when the SpecificationRevision was issued by the architect | [optional] 
**received_date** | **date** | The date when the SpecificationRevision was received by the project | [optional] 
**updated_at** | **str** | Updated at | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.specification_section_revision import SpecificationSectionRevision

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationSectionRevision from a JSON string
specification_section_revision_instance = SpecificationSectionRevision.from_json(json)
# print the JSON string representation of the object
print(SpecificationSectionRevision.to_json())

# convert the object into a dict
specification_section_revision_dict = specification_section_revision_instance.to_dict()
# create an instance of SpecificationSectionRevision from a dict
specification_section_revision_from_dict = SpecificationSectionRevision.from_dict(specification_section_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


