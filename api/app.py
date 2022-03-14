from ariadne import (ObjectType, graphql_sync, load_schema_from_path,
                     make_executable_schema, snake_case_fallback_resolvers)
from ariadne.constants import PLAYGROUND_HTML
from flask import jsonify, request

from api import app, db
from api.queries import (addStudent_resolver, createTimeTable_resolver,
                         deleteTimeTable_resolver, getStudent_resolver,
                         getTeacherTimeTable_resolver, getTimeTable_resolver,
                         listStudents_resolver)

db.create_all()
query = ObjectType("Query")
mutation=ObjectType("Mutation")
query.set_field("listStudents", listStudents_resolver)
query.set_field("getStudent", getStudent_resolver)
query.set_field("getTimeTable",getTimeTable_resolver)
query.set_field("getTeacherTimeTable",getTeacherTimeTable_resolver)
# query.set_field("addStudent", addStudent_resolver)
mutation.set_field("addStudent", addStudent_resolver)
mutation.set_field("createTimeTable",createTimeTable_resolver)
mutation.set_field("deleteTimeTable",deleteTimeTable_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs,query,mutation,snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__=="__main__":
    app.run(debug=True)
    